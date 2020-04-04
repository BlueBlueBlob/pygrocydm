from pygrocydm.grocy_api_client import GrocyApiClient, GrocyEntity
from pygrocydm.utils import parse_float, parse_int

QUANTITY_UNIT_CONVERTIONS_ENDPOINT = 'objects/quantity_unit_conversions'


class QuantityUnitConversion(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__from_qu_id = parse_int(parsed_json.get('from_qu_id'))
        self.__to_qu_id = parse_int(parsed_json.get('to_qu_id'))
        self.__factor = parse_float(parsed_json.get('factor'))
        self.__product_id = parse_int(parsed_json.get('product_id'))
        super().__init__(api, endpoint, parsed_json)

    @property
    def from_qu_id(self) -> int:
        return self.__from_qu_id

    @property
    def to_qu_id(self) -> int:
        return self.__to_qu_id

    @property
    def factor(self) -> float:
        return self.__factor

    @property
    def product_id(self) -> int:
        return self.__product_id
