from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_int

USEROBJECTS_ENDPOINT = 'objects/userobjects'


class UserObject(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__userentity_id = parse_int(parsed_json.get('userentity_id'))
        super().__init__(api, endpoint, parsed_json)

    @property
    def userentity_id(self) -> int:
        return self.__userentity_id
