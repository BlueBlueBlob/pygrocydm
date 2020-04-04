import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.userentity import USERENTITIES_ENDPOINT, UserEntity
from pygrocydm.grocy_api_client import GrocyApiClient


class TestUserEntity(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = USERENTITIES_ENDPOINT + '/1'

    def test_userentity_data_diff_valid(self):
        userentity = self.api.do_request("GET", self.endpoint)
        userentity_keys = userentity.keys()
        moked_userentity_json = """{
            "id": "1",
            "name": "exampleuserentity",
            "caption": "Example userentity",
            "description": "This is an example user entity...",
            "show_in_sidebar_menu": "1",
            "icon_css_class": "fas fa-smile",
            "row_created_timestamp": "2020-03-06 00:50:10"
        }"""
        moked_keys = json.loads(moked_userentity_json).keys()
        self.assertCountEqual(list(userentity_keys), list(moked_keys))

    def test_parse_json(self):
        userentity = UserEntity(self.api, USERENTITIES_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(userentity.id, int)
        assert isinstance(userentity.name, str)
        assert isinstance(userentity.caption, str)
        assert isinstance(userentity.description, str) or userentity.description is None
        assert isinstance(userentity.show_in_sidebar_menu, bool)
        assert isinstance(userentity.icon_css_class, str) or userentity.icon_css_class is None
        assert isinstance(userentity.row_created_timestamp, datetime)
