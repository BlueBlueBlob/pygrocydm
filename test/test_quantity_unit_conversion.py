import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.quantity_unit_conversion import QUANTITY_UNIT_CONVERTIONS_ENDPOINT, QuantityUnitConversion


class TestQuantityUnitConversion(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = f"{QUANTITY_UNIT_CONVERTIONS_ENDPOINT }/1"

    def test_quantity_unit_conversion_data_diff_valid(self):
        quantity_unit_conversion = self.api.do_request("GET", self.endpoint)
        quantity_unit_conversion_keys = quantity_unit_conversion.keys()
        moked_quantity_unit_conversion_json = """{
            "id": "1",
            "from_qu_id": "3",
            "to_qu_id": "12",
            "factor": "10.0",
            "product_id": "10",
            "row_created_timestamp": "2020-03-05 00:50:10"
        }"""
        moked_keys = json.loads(moked_quantity_unit_conversion_json).keys()
        self.assertCountEqual(list(quantity_unit_conversion_keys), list(moked_keys))

    def test_parse_json(self):
        quantity_unit_conversion = QuantityUnitConversion(self.api, QUANTITY_UNIT_CONVERTIONS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(quantity_unit_conversion.id, int)
        assert isinstance(quantity_unit_conversion.from_qu_id, int)
        assert isinstance(quantity_unit_conversion.to_qu_id, int)
        assert isinstance(quantity_unit_conversion.id, int)
        assert isinstance(quantity_unit_conversion.factor, float)
        assert isinstance(quantity_unit_conversion.product_id, int)
        assert isinstance(quantity_unit_conversion.row_created_timestamp, datetime)
