import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.quantity_unit import QUANTITY_UNITS_ENDPOINT, QuantityUnit


class TestQuantityUnit(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = QUANTITY_UNITS_ENDPOINT + '/2'

    def test_quantity_unit_data_diff_valid(self):
        quantity_unit = self.api.do_request("GET", self.endpoint)
        quantity_unit_keys = quantity_unit.keys()
        moked_quantity_unit_json = """{
            "id": "2",
            "name": "Piece",
            "description": null,
            "row_created_timestamp": "2020-03-04 00:50:13",
            "name_plural": "Pieces",
            "plural_forms": null
        }"""
        moked_keys = json.loads(moked_quantity_unit_json).keys()
        self.assertCountEqual(list(quantity_unit_keys), list(moked_keys))

    def test_parse_json(self):
        quantity_unit = QuantityUnit(self.api, QUANTITY_UNITS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(quantity_unit.id, int)
        assert isinstance(quantity_unit.description, str) or quantity_unit.description is None
        assert isinstance(quantity_unit.name, str)
        assert isinstance(quantity_unit.name_plural, str)
        assert isinstance(quantity_unit.plural_forms, str) or quantity_unit.plural_forms is None
        assert isinstance(quantity_unit.row_created_timestamp, datetime)
