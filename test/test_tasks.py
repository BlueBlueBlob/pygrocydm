import json
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase
from requests.exceptions import HTTPError
from datetime import datetime

from pygrocydm import GrocyAPI
from pygrocydm.tasks import TASKS_ENDPOINT, Task, Tasks
from pygrocydm.grocy_api_client import GrocyApiClient


class TestTask(TestCase):

    def setUp(self):
        self.grocy_api = GrocyAPI(CONST_BASE_URL, "demo_mode",  verify_ssl = CONST_SSL, port = CONST_PORT)
        self.api_client = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)

    def test_task_data_diff_valid(self): 
        task = self.api_client.do_request("GET", TASKS_ENDPOINT).pop()
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
        tasks = self.grocy_api.tasks()
        assert isinstance(tasks, Tasks)
        assert len(tasks.tasks_list) > 0
        for task in tasks.tasks_list:
            assert isinstance(task, Task)
            assert isinstance(task.id, int)
            assert isinstance(task.description, str) or not task.description
            assert isinstance(task.name, str)
            assert isinstance(task.due_date, (datetime, None)) or not task.description
            assert isinstance(task.done, bool)
            assert isinstance(task.done_timestamp, datetime) or not task.description
            assert isinstance(task.category_id, int) or not task.description
            assert isinstance(task.assigned_to_user_id, int)
            assert isinstance(task.row_created_timestamp, datetime)

    def test_complete_now(self):
        tasks = self.grocy_api.tasks()
        for task in tasks.tasks_list:
            if task.id == 1:
                task.complete()
                break
        tasks.refresh()
        for task in tasks.tasks_list:
            if task.id == 1:
                assert task.done

    def test_complete(self):
        test_time = datetime.now()
        tasks = self.grocy_api.tasks()
        for task in tasks.tasks_list:
            if task.id == 1:
                task.complete(test_time)
                break
        tasks.refresh()
        for task in tasks.tasks_list:
            if task.id == 1:
                assert task.done_timestamp == test_time

    def test_undo(self):
        tasks = self.grocy_api.tasks()
        for task in tasks.tasks_list:
            if task.id == 1:
                task.undo()
                break
        tasks.refresh()
        for task in tasks.tasks_list:
            if task.id == 1:
                assert not task.done
