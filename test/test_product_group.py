import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.product_group import PRODUCT_GROUPS_ENDPOINT, ProductGroup


class TestProductGroup(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = PRODUCT_GROUPS_ENDPOINT + '/1'

    def test_product_group_data_diff_valid(self):
        product_group = self.api.do_request("GET", self.endpoint)
        product_group_keys = product_group.keys()
        moked_product_group_json = """{
            "id": "1",
            "name": "01 Sweets",
            "description": null,
            "row_created_timestamp": "2020-03-05 00:50:10"
        }"""
        moked_keys = json.loads(moked_product_group_json).keys()
        self.assertCountEqual(list(product_group_keys), list(moked_keys))

    def test_parse_json(self):
        product_group = ProductGroup(self.api, PRODUCT_GROUPS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(product_group.id, int)
        assert isinstance(product_group.description, str) or product_group.description is None
        assert isinstance(product_group.name, str)
        assert isinstance(product_group.row_created_timestamp, datetime)
