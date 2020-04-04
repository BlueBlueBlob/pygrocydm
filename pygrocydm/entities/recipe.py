from enum import Enum

from pygrocydm.grocy_api_client import GrocyApiClient, GrocyEntity
from pygrocydm.utils import parse_bool, parse_int

RECIPES_ENDPOINT = 'objects/recipes'


class RecipeType(Enum):
    MEALPLAN_DAY = "mealplan-day"
    MEALPLAN_WEEK = "mealplan-week"
    NORMAL = "normal"


class Recipe(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__picture_file_name = parsed_json.get('picture_file_name', None)
        self.__base_servings = parse_int(parsed_json.get('base_servings'))
        self.__desired_servings = parse_int(
            parsed_json.get('desired_servings'))
        self.__not_check_shoppinglist = parse_bool(
            parsed_json.get('not_check_shoppinglist'), False)
        self.__type = parsed_json.get('type')
        self.__product_id = parse_int(parsed_json.get('product_id'), None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def picture_file_name(self) -> str:
        return self.__picture_file_name

    @property
    def base_servings(self) -> int:
        return self.__base_servings

    @property
    def desired_servings(self) -> int:
        return self.__desired_servings

    @property
    def not_check_shoppinglist(self) -> bool:
        return self.__not_check_shoppinglist

    @property
    def type(self) -> str:
        return self.__type

    @property
    def product_id(self) -> int:
        return self.__product_id
