import typing as t
from gettext import gettext

import click
import requests
from click import echo
from click._compat import get_text_stderr
from localstack import config
from localstack.cli.exceptions import CLIError
from localstack.pro.core.bootstrap.licensingv2 import LicensingError


class LicensingCLIError(CLIError):
    """A ClickException with a friendlier error message tailored to licensing errors."""

    def format_message(self) -> str:
        return (
            click.style("👋 This feature is part of our paid offering!", fg="yellow") + self.message
        )

    def show(self, file: t.Optional[t.IO[t.Any]] = None) -> None:
        if file is None:
            file = get_text_stderr()

        echo(gettext(self.format_message()), file=file)


class RequiresLicenseGroup(click.Group):
    """
    Special click command group that ensures a license was activated before invoking the command.
    """

    is_pro_command = True
    """Needed for localstack to properly group commands"""

    def invoke(self, ctx: click.Context) -> t.Any:
        from localstack.pro.core.bootstrap.licensingv2 import get_licensed_environment

        try:
            get_licensed_environment().activate_license()
        except LicensingError as e:
            raise LicensingCLIError(e.get_user_friendly_cli())

        return super().invoke(ctx)


class RequiresPlatformLicenseGroup(click.Group):
    """
    Base class for special click command groups that ensures a license includes a specified product.
    """

    namespace = "localstack.platform.plugin"
    # "paid" isn't a tier, but it avoids exposing "Pro"
    tier = "paid"

    # Needs to be provided by the specific feature to be gated
    name: str

    is_pro_command = True
    """Needed for localstack to properly group commands"""

    def invoke(self, ctx: click.Context) -> t.Any:
        try:
            if not self.is_feature_allowed():
                # TODO make this message more feature agnostic to allow for feature gating instead of tier gating message
                raise LicensingCLIError(f"""
=============================================
You tried to use a LocalStack feature that requires a {self.tier} subscription,
but the license did not contain the required subscription! 🔑❌

Due to this error, LocalStack has quit.

Please verify that your license includes the required tier for this feature. You can find your credentials in our
webapp at https://app.localstack.cloud.
""")
        except LicensingError as e:
            raise LicensingCLIError(e.get_user_friendly_cli())
        return super().invoke(ctx)

    def is_feature_allowed(self) -> bool:
        from localstack.pro.core.bootstrap.licensingv2 import get_licensed_environment

        licensed_environment = get_licensed_environment()
        licensed_environment.activate_license()

        product_name = f"{self.namespace}/{self.name}"
        return licensed_environment.has_product_license(product_name)


def _assert_host_reachable() -> None:
    """
    Ensures the host is up by opening the edge url. If a ConnectionRefusedError is raised it raises a ClickException -
    terminating with an error message.
    :raises: ClickException if the URL could not be reached
    """
    try:
        requests.get(config.external_service_url())
    except requests.ConnectionError:
        raise CLIError("Destination host unreachable. Please make sure LocalStack is running.")
