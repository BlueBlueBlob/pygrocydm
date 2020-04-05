import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase
from requests.exceptions import HTTPError

from pygrocydm import GrocyAPI
from pygrocydm.recipes import RECIPES_ENDPOINT, Recipe
from pygrocydm.grocy_api_client import GrocyApiClient


class TestRecipe(TestCase):

    def setUp(self):
        self.grocy_api = GrocyAPI(CONST_BASE_URL, "demo_mode",  verify_ssl = CONST_SSL, port = CONST_PORT)
        self.api_client = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = f"{RECIPES_ENDPOINT}/1/fulfillment"

    def test_recipe_data_diff_valid(self):
        recipe = self.api_client.do_request("GET", self.endpoint)
        recipe_keys = recipe.keys()
        moked_recipe_json = """{
            "id": "1",
            "recipe_id": "1",
            "need_fulfilled": "0",
            "need_fulfilled_with_shopping_list": "0",
            "missing_products_count": "4",
            "costs": "24.25",
            "calories": "492.0"
            }"""
        moked_keys = json.loads(moked_recipe_json).keys()
        self.assertCountEqual(list(recipe_keys), list(moked_keys))

    def test_parse_json(self):
        recipe = Recipe(self.api_client, self.api_client.do_request("GET", self.endpoint))
        assert isinstance(recipe.id, int)
        assert isinstance(recipe.recipe_id, int)
        assert isinstance(recipe.need_fulfilled, bool)
        assert isinstance(recipe.need_fulfilled_with_shopping_list, bool)
        assert isinstance(recipe.missing_products_count, int)
        assert isinstance(recipe.costs, float)
        assert isinstance(recipe.calories, float)

    def test_add_product(self):
        recipes = self.grocy_api.recipes().fullfilment_list
        for recipe in recipes:
            if recipe.recipe_id == 2:
                recipe.add_not_fulfilled_products_to_shoppinglist()
                break

    def test_add_product_exclude(self):
        recipes = self.grocy_api.recipes().fullfilment_list
        for recipe in recipes:
            if recipe.recipe_id == 2:
                recipe.add_not_fulfilled_products_to_shoppinglist([17])
                break

    def test_consume_valid(self):
        recipes = self.grocy_api.recipes().fullfilment_list
        for recipe in recipes:
            if recipe.recipe_id == 3:
                recipe.consume()
                break

    def test_consume_error(self):
        recipes = self.grocy_api.recipes().fullfilment_list
        for recipe in recipes:
            if recipe.recipe_id == 0:
                self.assertRaises(HTTPError, recipe.consume)
