import json
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase
from requests.exceptions import HTTPError
from datetime import date, datetime

from pygrocydm import GrocyAPI
from pygrocydm.system import SYSTEM_ENDPOINT, System
from pygrocydm.grocy_api_client import GrocyApiClient


class TestSystem(TestCase):

    def setUp(self):
        self.grocy_api = GrocyAPI(CONST_BASE_URL, "demo_mode",  verify_ssl = CONST_SSL, port = CONST_PORT)
        self.api_client = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)


    def test_versions(self):
        system = self.grocy_api.system()
        self.assertIsInstance(system, System)
        self.assertIsInstance(system.grocy_version, str)
        self.assertIsInstance(system.grocy_release_date(), date)
        self.assertIsInstance(system.php_version, str)
        self.assertIsInstance(system.sqlite_version, str)

    def test_db_changed_time(self):
        db_time = self.grocy_api.system().db_changed_time()
        self.assertIsInstance(db_time, datetime)

