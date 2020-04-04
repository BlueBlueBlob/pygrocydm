import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.equipment import EQUIPMENT_ENDPOINT, Equipment


class TestEquipment(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = EQUIPMENT_ENDPOINT + '/1'

    def test_equipment_data_diff_valid(self):
        equipment = self.api.do_request("GET", self.endpoint)
        equipment_keys = equipment.keys()
        moked_equipment_json = """{
            "id": "1",
            "name": "Coffee machine",
            "description": null,
            "row_created_timestamp": "2020-03-05 00:50:10",
            "instruction_manual_file_name": "loremipsum.pdf"
        }"""
        moked_keys = json.loads(moked_equipment_json).keys()
        self.assertCountEqual(list(equipment_keys), list(moked_keys))

    def test_parse_json(self):
        equipment = Equipment(self.api, EQUIPMENT_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(equipment.id, int)
        assert isinstance(equipment.description, str) or equipment.description is None
        assert isinstance(equipment.name, str)
        assert isinstance(equipment.instruction_manual_file_name, str) or not equipment.instruction_manual_file_name
        assert isinstance(equipment.row_created_timestamp, datetime)
