import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.task_category import TASK_CATEGORIES_ENDPOINT, TaskCategory


class TestTaskCategory(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = TASK_CATEGORIES_ENDPOINT + '/1'

    def test_task_category_data_diff_valid(self):
        task_category = self.api.do_request("GET", self.endpoint)
        task_category_keys = task_category.keys()
        moked_task_category_json = """{
            "id": "1",
            "name": "Home",
            "description": null,
            "row_created_timestamp": "2020-03-05 00:50:10"
        }"""
        moked_keys = json.loads(moked_task_category_json).keys()
        self.assertCountEqual(list(task_category_keys), list(moked_keys))

    def test_parse_json(self):
        task_category = TaskCategory(self.api, TASK_CATEGORIES_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(task_category.id, int)
        assert isinstance(task_category.description, str) or task_category.description is None
        assert isinstance(task_category.name, str)
        assert isinstance(task_category.row_created_timestamp, datetime)
