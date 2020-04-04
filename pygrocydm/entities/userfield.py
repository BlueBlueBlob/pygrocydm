from enum import Enum

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_bool

USERFIELDS_ENDPOINT = 'objects/userfields'


class UserfieldType(Enum):
    TEXT_SINGLE_LINE = "text-single-line"
    TEXT_MULTI_LINE = "text-multi-line"
    NUMBER_INTEGRAL = "number-integral"
    NUMBER_DECIMAL = "number-decimal"
    DATE = "date"
    DATETIME = "datetime"
    CHECKBOX = "checkbox"
    LINK = "link"
    PRESET_LIST = "preset-list"
    PRESET_CHECKLIST = "preset-checklist"


class Userfield(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__entity = parsed_json.get('entity')
        self.__name = parsed_json.get('name')
        self.__caption = parsed_json.get('caption')
        self.__type = parsed_json.get('type')
        self.__show_as_column_in_tables = parse_bool(
            parsed_json.get('show_as_column_in_tables'), False)
        self.__config = parsed_json.get('config', None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def entity(self) -> str:
        return self.__entity

    @property
    def name(self) -> str:
        return self.__name

    @property
    def caption(self) -> str:
        return self.__caption

    @property
    def type(self) -> str:
        return self.__type

    @property
    def show_as_column_in_tables(self) -> bool:
        return self.__show_as_column_in_tables

    @property
    def config(self) -> str:
        return self.__config
