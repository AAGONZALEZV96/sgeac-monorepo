from enum import Enum
class MergeStrategy(str,Enum):OVERWRITE='overwrite';ACCOUNT_REGION_MERGE='account-region-merge';SERVICE_MERGE='service-merge'
DEFAULT_STRATEGY=MergeStrategy.ACCOUNT_REGION_MERGE.value