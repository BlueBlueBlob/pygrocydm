import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.task import TASKS_ENDPOINT, Task
from pygrocydm.grocy_api_client import GrocyApiClient


class TestTask(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = TASKS_ENDPOINT + '/1'

    def test_task_data_diff_valid(self):
        task = self.api.do_request("GET", self.endpoint)
        task_keys = task.keys()
        moked_task_json = """{
            "id": "1",
            "name": "Repair the garage door",
            "description": null,
            "due_date": "2020-03-18",
            "done": "0",
            "done_timestamp": null,
            "category_id": "1",
            "assigned_to_user_id": "1",
            "row_created_timestamp": "2020-03-04 00:50:14"
        }"""
        moked_keys = json.loads(moked_task_json).keys()
        self.assertCountEqual(list(task_keys), list(moked_keys))

    def test_parse_json(self):
        task = Task(self.api, TASKS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(task.id, int)
        assert isinstance(task.description, str) or not task.description
        assert isinstance(task.name, str)
        assert isinstance(task.due_date, (datetime, None)) or not task.description
        assert isinstance(task.done, bool)
        assert isinstance(task.done_timestamp, datetime) or not task.description
        assert isinstance(task.category_id, int) or not task.description
        assert isinstance(task.assigned_to_user_id, int)
        assert isinstance(task.row_created_timestamp, datetime)
