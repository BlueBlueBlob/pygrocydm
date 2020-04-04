from enum import Enum

from pygrocydm.grocy_api_client import GrocyApiClient, GrocyEntity
from pygrocydm.utils import parse_bool, parse_int

CHORES_ENDPOINT = 'objects/chores'


class PeriodType(Enum):
    MANUALLY = "manually"
    DYNAMIC_REGULAR = "dynamic-regular"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class AssignmentType(Enum):
    NO_ASSIGNMENT = "no-assignment"
    WHO_LEAST_DID_FIRST = "who-least-did-first"
    RANDOM = "random"
    IN_ALPHABETICAL_ORDER = "in-alphabetical-order"


class Chore(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__period_type = parsed_json.get('period_type')
        self.__period_config = parsed_json.get('period_config', None)
        self.__period_days = parse_int(parsed_json.get('period_days'), None)
        self.__track_date_only = parse_bool(
            parsed_json.get('track_date_only'), False)
        self.__rollover = parse_bool(parsed_json.get('rollover'), False)
        self.__assignment_type = parsed_json.get('assignment_type', None)
        self.__assignment_config = parsed_json.get('assignment_config', None)
        self.__next_execution_assigned_to_user_id = parse_int(
            parsed_json.get('next_execution_assigned_to_user_id'),
            None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def period_type(self) -> str:
        return self.__period_type

    @property
    def period_config(self) -> str:
        return self.__period_config

    @property
    def period_days(self) -> int:
        return self.__period_days

    @property
    def track_date_only(self) -> bool:
        return self.__track_date_only

    @property
    def rollover(self) -> bool:
        return self.__rollover

    @property
    def assignment_type(self) -> str:
        return self.__assignment_type

    @property
    def assignment_config(self) -> str:
        return self.__assignment_config

    @property
    def next_execution_assigned_to_user_id(self) -> int:
        return self.__next_execution_assigned_to_user_id
