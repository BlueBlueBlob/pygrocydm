import json
from datetime import datetime
from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

from pygrocydm.grocy_api_client import GrocyApiClient
from pygrocydm.entities.product import Product, PRODUCTS_ENDPOINT


class TestProduct(TestCase):

    def setUp(self):
        self.api = GrocyApiClient(CONST_BASE_URL, "demo_mode",  verify_ssl=CONST_SSL, port=CONST_PORT)
        self.endpoint = 'objects/products/1'

    def test_product_data_diff_valid(self):
        product = self.api.do_request("GET", self.endpoint)
        product_keys = product.keys()
        moked_product_json = """{
            "id": "1",
            "name": "Cookies",
            "description": null,
            "location_id": "4",
            "qu_id_purchase": "3",
            "qu_id_stock": "3",
            "qu_factor_purchase_to_stock": "1.0",
            "barcode": null,
            "min_stock_amount": "8",
            "default_best_before_days": "0",
            "row_created_timestamp": "2020-02-25 00:50:13",
            "product_group_id": "1",
            "picture_file_name": "cookies.jpg",
            "default_best_before_days_after_open": "0",
            "allow_partial_units_in_stock": "0",
            "enable_tare_weight_handling": "0",
            "tare_weight": "0.0",
            "not_check_stock_fulfillment_for_recipes": "0",
            "parent_product_id": null,
            "calories": "123",
            "cumulate_min_stock_amount_of_sub_products": "0",
            "default_best_before_days_after_freezing": "0",
            "default_best_before_days_after_thawing": "0"
        }"""
        moked_keys = json.loads(moked_product_json).keys()
        self.assertCountEqual(list(product_keys), list(moked_keys))

    def test_parse_json(self):
        product = Product(self.api, PRODUCTS_ENDPOINT, self.api.do_request("GET", self.endpoint))
        assert isinstance(product.id, int)
        assert isinstance(product.product_group_id, int)
        assert isinstance(product.name, str)
        assert isinstance(product.barcodes, (str, list)) or product.barcodes is None
        assert isinstance(product.location_id, int) or product.location_id is None
        assert isinstance(product.qu_id_purchase, int) or product.qu_id_purchase is None
        assert isinstance(product.description, str) or product.description is None
        assert isinstance(product.qu_id_stock, int) or product.qu_id_stock is None
        assert isinstance(product.enable_tare_weight_handling, int) or product.enable_tare_weight_handling is None
        assert isinstance(product.not_check_stock_fulfillment_for_recipes, int) or product.not_check_stock_fulfillment_for_recipes is None
        assert isinstance(product.qu_factor_purchase_to_stock, float) or product.qu_factor_purchase_to_stock is None
        assert isinstance(product.tare_weight, float) or product.tare_weight is None
        assert isinstance(product.min_stock_amount, int) or product.min_stock_amount == 0
        assert isinstance(product.default_best_before_days, int) or product.default_best_before_days is None
        assert isinstance(product.default_best_before_days_after_open, int) or product.default_best_before_days_after_open is None
        assert isinstance(product.picture_file_name, str) or product.picture_file_name is None
        assert isinstance(product.allow_partial_units_in_stock, bool)
        assert isinstance(product.row_created_timestamp, datetime)
