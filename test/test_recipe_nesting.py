import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.recipe_nesting import RECIPES_NESTINGS_ENDPOINT, RecipeNesting
from pygrocydm.grocy_api_client import GrocyApiClient


class TestRecipeNesting(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = RECIPES_NESTINGS_ENDPOINT + '/1'

    def test_recipe_nesting_data_diff_valid(self):
        recipe_nesting = self.api.do_request("GET", self.endpoint)
        recipe_nesting_keys = recipe_nesting.keys()
        moked_recipe_nesting_json = """{
            "id": "1",
            "recipe_id": "6",
            "includes_recipe_id": "4",
            "row_created_timestamp": "2020-03-12 00:50:11",
            "servings": "1"
        }"""
        moked_keys = json.loads(moked_recipe_nesting_json).keys()
        self.assertCountEqual(list(recipe_nesting_keys), list(moked_keys))

    def test_parse_json(self):
        recipe_nesting = RecipeNesting(self.api, RECIPES_NESTINGS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(recipe_nesting.id, int)
        assert isinstance(recipe_nesting.recipe_id, int)
        assert isinstance(recipe_nesting.includes_recipe_id, int)
        assert isinstance(recipe_nesting.servings, int)
        assert isinstance(recipe_nesting.row_created_timestamp, datetime)
