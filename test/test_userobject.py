import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.userobject import USEROBJECTS_ENDPOINT, UserObject
from pygrocydm.grocy_api_client import GrocyApiClient


class TestUserEntity(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = USEROBJECTS_ENDPOINT + '/1'

    def test_userobject_data_diff_valid(self):
        userobject = self.api.do_request("GET", self.endpoint)
        userobject_keys = userobject.keys()
        moked_userobject_json = """{
            "id": "1",
            "userentity_id": "1",
            "row_created_timestamp": "2020-03-06 00:50:10"
        }"""
        moked_keys = json.loads(moked_userobject_json).keys()
        self.assertCountEqual(list(userobject_keys), list(moked_keys))

    def test_parse_json(self):
        userobject = UserObject(self.api, USEROBJECTS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(userobject.id, int)
        assert isinstance(userobject.userentity_id, int)
        assert isinstance(userobject.row_created_timestamp, datetime)
