import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.meal_plan import MEAL_PLAN_ENDPOINT, MealPlan, MealPlanType
from pygrocydm.grocy_api_client import GrocyApiClient


class TestMealPlan(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = MEAL_PLAN_ENDPOINT + '/1'

    def test_meal_plan_data_diff_valid(self):
        meal_plan = self.api.do_request("GET", self.endpoint)
        meal_plan_keys = meal_plan.keys()
        moked_meal_plan_json = """{
            "id": "1",
            "day": "2020-03-09",
            "type": "recipe",
            "recipe_id": "1",
            "recipe_servings": "1",
            "note": null,
            "product_id": null,
            "product_amount": "0.0",
            "product_qu_id": null,
            "row_created_timestamp": "2020-03-11 00:50:12"
          }"""
        moked_keys = json.loads(moked_meal_plan_json).keys()
        self.assertCountEqual(list(meal_plan_keys), list(moked_keys))

    def test_parse_json(self):
        meal_types = { item.value for item in MealPlanType }
        meal_plan = MealPlan(self.api, MEAL_PLAN_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(meal_plan.id, int)
        assert isinstance(meal_plan.day, datetime)
        assert (isinstance(meal_plan.type, str) and meal_plan.type in meal_types)
        assert isinstance(meal_plan.recipe_id, int) or meal_plan.recipe_id is None
        assert isinstance(meal_plan.recipe_servings, int) or meal_plan.recipe_servings is None
        assert isinstance(meal_plan.note, str) or meal_plan.note is None
        assert isinstance(meal_plan.product_id, int) or meal_plan.product_id is None
        assert isinstance(meal_plan.product_amount, float)
        assert isinstance(meal_plan.product_qu_id, int) or not meal_plan.product_qu_id
        assert isinstance(meal_plan.row_created_timestamp, datetime)
