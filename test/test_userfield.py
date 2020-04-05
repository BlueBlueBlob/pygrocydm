import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.userfield import USERFIELDS_ENDPOINT, Userfield, UserfieldType
from pygrocydm.grocy_api_client import GrocyApiClient


class TestUserfield(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = USERFIELDS_ENDPOINT + '/1'

    def test_userfield_data_diff_valid(self):
        userfield = self.api.do_request("GET", self.endpoint)
        userfield_keys = userfield.keys()
        moked_userfield_json = """{
            "id": "1",
            "entity": "userentity-exampleuserentity",
            "name": "customfield1",
            "caption": "Custom field 1",
            "type": "text-single-line",
            "show_as_column_in_tables": "1",
            "row_created_timestamp": "2020-03-06 00:50:10",
            "config": null
        }"""
        moked_keys = json.loads(moked_userfield_json).keys()
        self.assertCountEqual(list(userfield_keys), list(moked_keys))

    def test_parse_json(self):
        uf_types = { item.value for item in UserfieldType }
        userfield = Userfield(self.api, USERFIELDS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(userfield.id, int)
        assert isinstance(userfield.entity, str)
        assert isinstance(userfield.name, str)
        assert isinstance(userfield.caption, str)
        assert isinstance(userfield.type, str) and userfield.type in uf_types
        assert isinstance(userfield.show_as_column_in_tables, bool)
        assert isinstance(userfield.config, str) or userfield.config is None
        assert isinstance(userfield.row_created_timestamp, datetime)
