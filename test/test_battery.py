import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.battery import BATTERIES_ENDPOINT, Battery
from pygrocydm.grocy_api_client import GrocyApiClient


class TestBattery(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = BATTERIES_ENDPOINT + '/1'

    def test_battery_data_diff_valid(self):
        battery = self.api.do_request("GET", self.endpoint)
        battery_keys = battery.keys()
        moked_battery_json = """{
            "id": "1",
            "name": "Battery1",
            "description": "Warranty ends 2023",
            "used_in": "TV remote control",
            "charge_interval_days": "0",
            "row_created_timestamp": "2020-03-01 00:50:25"
        }"""
        moked_keys = json.loads(moked_battery_json).keys()
        self.assertCountEqual(list(battery_keys), list(moked_keys))

    def test_parse_json(self):
        battery = Battery(self.api, BATTERIES_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(battery.id, int)
        assert isinstance(battery.description, str) or battery.description is None
        assert isinstance(battery.name, str)
        assert isinstance(battery.used_in, (str, None))
        assert isinstance(battery.charge_interval_days, int)
        assert isinstance(battery.row_created_timestamp, datetime)
