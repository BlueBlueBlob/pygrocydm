import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.entities.chore import CHORES_ENDPOINT, Chore, PeriodType, AssignmentType
from pygrocydm.grocy_api_client import GrocyApiClient


class TestChore(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = CHORES_ENDPOINT + '/1'

    def test_chore_data_diff_valid(self):
        chore = self.api.do_request("GET", self.endpoint)
        chore_keys = chore.keys()
        moked_chore_json = """{
            "id": "1",
            "name": "Changed towels in the bathroom",
            "description": null,
            "period_type": "manually",
            "period_days": "5",
            "row_created_timestamp": "2020-02-26 00:50:11",
            "period_config": null,
            "track_date_only": "0",
            "rollover": "0",
            "assignment_type": null,
            "assignment_config": null,
            "next_execution_assigned_to_user_id": null,
            "consume_product_on_execution": "0",
            "product_id": null,
            "product_amount": null,
            "period_interval": "1"
        }"""
        moked_keys = json.loads(moked_chore_json).keys()
        self.assertCountEqual(list(chore_keys), list(moked_keys))

    def test_parse_json(self):
        assignment_types = { item.value for item in AssignmentType }
        period_types = { item.value for item in PeriodType }
        chore = Chore(self.api, CHORES_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(chore.id, int)
        assert isinstance(chore.description, str) or chore.description is None
        assert isinstance(chore.name, str)
        assert isinstance(chore.period_type, str) and chore.period_type in period_types
        assert isinstance(chore.period_days, int) or chore.period_days is None
        assert isinstance(chore.next_execution_assigned_to_user_id, int) or chore.next_execution_assigned_to_user_id is None
        assert isinstance(chore.description, str) or chore.description is None
        assert isinstance(chore.period_config, str) or chore.period_config is None
        assert isinstance(chore.track_date_only, bool) or not chore.track_date_only
        assert isinstance(chore.rollover, bool) or not chore.rollover
        assert (isinstance(chore.assignment_type, str) and chore.assignment_type in assignment_types) or chore.assignment_type is None
        assert isinstance(chore.assignment_config, str) or chore.assignment_config is None
        assert isinstance(chore.row_created_timestamp, datetime)
