from pygrocydm.grocy_api_client import GrocyApiClient, GrocyEntity
from pygrocydm.utils import parse_bool, parse_int, parse_float

RECIPES_POS_ENDPOINT = 'objects/recipes_pos'


class RecipePos(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__recipe_id = parse_int(parsed_json.get('recipe_id'))
        self.__product_id = parse_int(parsed_json.get('product_id'))
        self.__amount = parse_float(parsed_json.get('amount'))
        self.__note = parsed_json.get('note', None)
        self.__qu_id = parse_int(parsed_json.get('qu_id'))
        self.__only_check_single_unit_in_stock = parse_bool(
            parsed_json.get('only_check_single_unit_in_stock'), False)
        self.__ingredient_group = parsed_json.get('ingredient_group', None)
        self.__not_check_stock_fulfillment = parse_bool(
            parsed_json.get('not_check_stock_fulfillment'), False)
        self.__variable_amount = parsed_json.get('variable_amount', None)
        self.__price_factor = parse_float(parsed_json.get('price_factor'))
        super().__init__(api, endpoint, parsed_json)

    @property
    def recipe_id(self) -> int:
        return self.__recipe_id

    @property
    def product_id(self) -> int:
        return self.__product_id

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def note(self) -> str:
        return self.__note

    @property
    def qu_id(self) -> int:
        return self.__qu_id

    @property
    def only_check_single_unit_in_stock(self) -> bool:
        return self.__only_check_single_unit_in_stock

    @property
    def ingredient_group(self) -> str:
        return self.__ingredient_group

    @property
    def not_check_stock_fulfillment(self) -> bool:
        return self.__not_check_stock_fulfillment

    @property
    def variable_amount(self) -> str:
        return self.__variable_amount

    @property
    def price_factor(self) -> float:
        return self.__price_factor
