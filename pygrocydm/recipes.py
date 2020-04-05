from .grocy_api_client import GrocyApiClient
from .utils import parse_int, parse_bool, parse_float
from typing import List, Tuple
import json


RECIPES_ENDPOINT = 'recipes'


class Recipe():
    def __init__(self, api_client: GrocyApiClient, parsed_json):
        self.__api_client = api_client
        self.__id = parse_int(parsed_json.get('id'))
        self.__recipe_id = parse_int(parsed_json.get('recipe_id'))
        self.__endpoint = f"{RECIPES_ENDPOINT}/{self.__recipe_id}"
        self.__need_fulfilled = parse_bool(
            parsed_json.get('need_fulfilled'), False)
        self.__need_fulfilled_with_shopping_list = parse_bool(
            parsed_json.get('need_fulfilled_with_shopping_list'), False)
        self.__missing_products_count = parse_int(parsed_json.get('missing_products_count'))
        self.__costs = parse_float(parsed_json.get('costs'), 0)
        self.__calories = parse_float(parsed_json.get('calories'), 0)

    def add_not_fulfilled_products_to_shoppinglist(self, exclude_products: List[int] = None):
        endpoint = f"{self.__endpoint}/add-not-fulfilled-products-to-shoppinglist"
        data = {}
        if exclude_products:
            data['excludedProductIds'] = exclude_products
        else:
            data['excludedProductIds'] = [0]
        self.__api_client.do_request("POST", endpoint, json.dumps(data))

    def consume(self):
        endpoint = f"{self.__endpoint}/consume"
        self.__api_client.do_request("POST", endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def recipe_id(self) -> int:
        return self.__recipe_id

    @property
    def need_fulfilled(self) -> bool:
        return self.__need_fulfilled

    @property
    def need_fulfilled_with_shopping_list(self) -> bool:
        return self.__need_fulfilled_with_shopping_list

    @property
    def missing_products_count(self) -> int:
        return self.__missing_products_count

    @property
    def costs(self) -> float:
        return self.__costs

    @property
    def calories(self) -> float:
        return self.__calories


class Recipes():
    def __init__(self, api_client: GrocyApiClient):
        self.__api_client = api_client
        self.__fullfilment_list = ()
        self.refresh()

    def refresh(self):
        endpoint = f"{RECIPES_ENDPOINT}/fulfillment"
        parsed_json = self.__api_client.do_request("GET", endpoint)
        if parsed_json:
            self.__fullfilment_list = ([ Recipe(self.__api_client, response) for response in parsed_json ])

    @property
    def fullfilment_list(self) -> Tuple[Recipe]:
        return self.__fullfilment_list
