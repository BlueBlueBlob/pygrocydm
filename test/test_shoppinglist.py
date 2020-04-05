import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.shopping_list import (SHOPPING_LIST_ENDPOINT,
                                     SHOPPING_LISTS_ENDPOINT, ShoppingList,
                                     ShoppingListItem)


class TestShoppingList(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = SHOPPING_LISTS_ENDPOINT + '/1'

    def test_shopping_list_data_diff_valid(self):
        shopping_list = self.api.do_request("GET", self.endpoint)
        shopping_list_keys = shopping_list.keys()
        moked_shopping_list_json = """{
            "id": "1",
            "name": "Shopping list",
            "description": null,
            "row_created_timestamp": "2020-03-02 00:50:09"
        }"""
        moked_keys = json.loads(moked_shopping_list_json).keys()
        self.assertCountEqual(list(shopping_list_keys), list(moked_keys))

    def test_parse_json(self):
        shopping_list = ShoppingList(self.api, SHOPPING_LIST_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(shopping_list.id, int)
        assert isinstance(shopping_list.description, str) or shopping_list.description is None
        assert isinstance(shopping_list.name, str)
        assert isinstance(shopping_list.row_created_timestamp, datetime)


class TestShoppingListItem(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = SHOPPING_LIST_ENDPOINT + '/1'

    def test_shopping_list_item_data_diff_valid(self):
        shopping_list_item = self.api.do_request("GET", self.endpoint)
        shopping_list_item_keys = shopping_list_item.keys()
        moked_shopping_list_item_json = """{
            "id": "1",
            "product_id": null,
            "note": "Some good snacks",
            "amount": "1",
            "row_created_timestamp": "2020-03-02 00:50:10",
            "shopping_list_id": "1",
            "done": "0"
        }"""
        moked_keys = json.loads(moked_shopping_list_item_json).keys()
        self.assertCountEqual(list(shopping_list_item_keys), list(moked_keys))

    def test_parse_json(self):
        shopping_list_item = ShoppingListItem(self.api, SHOPPING_LISTS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(shopping_list_item.id, int)
        assert isinstance(shopping_list_item.product_id, int) or shopping_list_item.product_id is None
        assert isinstance(shopping_list_item.note, str) or shopping_list_item.note is None
        assert isinstance(shopping_list_item.amount, float)
        assert isinstance(shopping_list_item.shopping_list_id, int)
        assert isinstance(shopping_list_item.done, bool)
        assert isinstance(shopping_list_item.row_created_timestamp, datetime)
