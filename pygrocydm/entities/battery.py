from pygrocydm.grocy_api_client import GrocyApiClient, GrocyEntity
from pygrocydm.utils import parse_int

BATTERIES_ENDPOINT = 'objects/batteries'


class Battery(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__used_in = parsed_json.get('used_in', None)
        self.__charge_interval_days = parse_int(
            parsed_json.get('charge_interval_days'),
            0)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def used_in(self) -> str:
        return self.__used_in

    @property
    def charge_interval_days(self) -> int:
        return self.__charge_interval_days
