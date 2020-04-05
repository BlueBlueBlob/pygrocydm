import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.recipe import RECIPES_ENDPOINT, Recipe, RecipeType
from pygrocydm.grocy_api_client import GrocyApiClient


class TestRecipe(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = RECIPES_ENDPOINT + '/1'

    def test_recipe_data_diff_valid(self):
        recipe = self.api.do_request("GET", self.endpoint)
        recipe_keys = recipe.keys()
        moked_recipe_json = """{
            "id": "-35",
            "name": "2020-11",
            "description": null,
            "row_created_timestamp": "2020-03-11 11:12:23",
            "picture_file_name": null,
            "base_servings": "1",
            "desired_servings": "1",
            "not_check_shoppinglist": "0",
            "type": "mealplan-week",
            "product_id": null
          }"""
        moked_keys = json.loads(moked_recipe_json).keys()
        self.assertCountEqual(list(recipe_keys), list(moked_keys))

    def test_parse_json(self):
        recipe_types = { item.value for item in RecipeType }
        recipe = Recipe(self.api, RECIPES_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(recipe.id, int)
        assert isinstance(recipe.name, str)
        assert (isinstance(recipe.type, str) and recipe.type in recipe_types)
        assert isinstance(recipe.description, str) or recipe.description is None
        assert isinstance(recipe.base_servings, int)
        assert isinstance(recipe.desired_servings, int)
        assert isinstance(recipe.picture_file_name, str) or recipe.picture_file_name is None
        assert isinstance(recipe.not_check_shoppinglist, bool)
        assert isinstance(recipe.product_id, int) or not recipe.product_id
        assert isinstance(recipe.row_created_timestamp, datetime)
