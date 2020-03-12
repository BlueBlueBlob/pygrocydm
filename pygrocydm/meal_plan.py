from enum import Enum
from datetime import datetime

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_float, parse_int, parse_date

MEAL_PLAN_ENDPOINT = 'objects/meal_plan'


class MealPlanType(Enum):
    NOTE = "note"
    PRODUCT = "product"
    RECIPE = "recipe"


class MealPlan(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__day = parse_date(parsed_json.get('day'))
        self.__type = parsed_json.get('type')
        self.__recipe_id = parse_int(parsed_json.get('recipe_id'), None)
        self.__recipe_servings = parse_int(
            parsed_json.get('recipe_servings'), None)
        self.__note = parsed_json.get('note', None)
        self.__product_id = parse_int(
            parsed_json.get('product_id'), None)
        self.__product_amount = parse_float(
            parsed_json.get('product_amount'), 0)
        self.__product_qu_id = parse_int(
            parsed_json.get('product_qu_id'), None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def day(self) -> datetime:
        return self.__day

    @property
    def type(self) -> str:
        return self.__type

    @property
    def recipe_id(self) -> int:
        return self.__recipe_id

    @property
    def recipe_servings(self) -> int:
        return self.__recipe_servings

    @property
    def note(self) -> str:
        return self.__note

    @property
    def product_id(self) -> int:
        return self.__product_id

    @property
    def product_amount(self) -> float:
        return self.__product_amount

    @property
    def product_qu_id(self) -> id:
        return self.__product_qu_id
