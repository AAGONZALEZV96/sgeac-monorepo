from localstack.pro.core.testing.testselection.matching import MATCHING_RULES_EXT
from localstack.pro.core.testing.testselection.opt_out import OPT_OUT
from localstack.testing.testselection.scripts.generate_test_selection import generate_test_selection
if __name__=='__main__':generate_test_selection(opt_out=OPT_OUT,matching_rules=MATCHING_RULES_EXT,repo_name='localstack_ext')