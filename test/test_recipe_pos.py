import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.recipe_pos import RECIPES_POS_ENDPOINT, RecipePos
from pygrocydm.grocy_api_client import GrocyApiClient


class TestRecipePos(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = RECIPES_POS_ENDPOINT + '/1'

    def test_recipe_pos_data_diff_valid(self):
        recipe_pos = self.api.do_request("GET", self.endpoint)
        recipe_pos_keys = recipe_pos.keys()
        moked_recipe_pos_json = """{
            "id": "1",
            "recipe_id": "1",
            "product_id": "16",
            "amount": "1.0",
            "note": null,
            "qu_id": "3",
            "only_check_single_unit_in_stock": "0",
            "ingredient_group": "Bottom",
            "not_check_stock_fulfillment": "0",
            "row_created_timestamp": "2020-03-12 00:50:11",
            "variable_amount": null,
            "price_factor": "1.0"
          }"""
        moked_keys = json.loads(moked_recipe_pos_json).keys()
        self.assertCountEqual(list(recipe_pos_keys), list(moked_keys))

    def test_parse_json(self):
        recipe_pos = RecipePos(self.api, RECIPES_POS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(recipe_pos.id, int)
        assert isinstance(recipe_pos.recipe_id, int)
        assert isinstance(recipe_pos.product_id, int)
        assert isinstance(recipe_pos.amount, float)
        assert isinstance(recipe_pos.note, str) or recipe_pos.note is None
        assert isinstance(recipe_pos.qu_id, int)
        assert isinstance(recipe_pos.only_check_single_unit_in_stock, bool)
        assert isinstance(recipe_pos.ingredient_group, str) or recipe_pos.ingredient_group is None
        assert isinstance(recipe_pos.not_check_stock_fulfillment, bool)
        assert isinstance(recipe_pos.variable_amount, str) or not recipe_pos.variable_amount
        assert isinstance(recipe_pos.price_factor, float)
        assert isinstance(recipe_pos.row_created_timestamp, datetime)
