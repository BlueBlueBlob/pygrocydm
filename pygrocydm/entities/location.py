from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_bool

LOCATION_ENDPOINT = 'objects/locations'


class Location(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__is_freezer = parse_bool(parsed_json.get('is_freezer'), False)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def is_freezer(self) -> bool:
        return self.__is_freezer
