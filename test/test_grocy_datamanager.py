from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL
from unittest import TestCase

import responses
from requests.exceptions import HTTPError

from pygrocydm import GrocyDataManager
from pygrocydm.battery import Battery
from pygrocydm.chore import Chore
from pygrocydm.equipment import Equipment
from pygrocydm.location import Location
from pygrocydm.meal_plan import MealPlan
from pygrocydm.product import Product
from pygrocydm.product_group import ProductGroup
from pygrocydm.quantity_unit import QuantityUnit
from pygrocydm.quantity_unit_conversion import QuantityUnitConversion
from pygrocydm.recipe import Recipe
from pygrocydm.recipe_pos import RecipePos
from pygrocydm.shopping_list import ShoppingList, ShoppingListItem
from pygrocydm.task import Task
from pygrocydm.task_category import TaskCategory
from pygrocydm.userentity import UserEntity
from pygrocydm.userfield import Userfield
from pygrocydm.userobject import UserObject


class TestGrocyDataManager(TestCase):

    def setUp(self):
        self.gdm = GrocyDataManager(CONST_BASE_URL, "api_key")
        self.gdm = None
        self.gdm = GrocyDataManager(CONST_BASE_URL, "demo_mode",  verify_ssl = CONST_SSL, port = CONST_PORT)

    def test_init(self):
        assert isinstance(self.gdm, GrocyDataManager)

    def test_products_valid(self):
        products = self.gdm.products().list
        assert isinstance(products, tuple)
        assert len(products) >=1
        for product in products:
            assert isinstance(product, Product)

    @responses.activate
    def test_products_invalid_no_data(self):
        resp = []
        responses.add(responses.GET,
            f"{CONST_BASE_URL}:{CONST_PORT}/api/objects/products",
            json=resp,
            status=200)
        products = self.gdm.products().list
        assert len(products) == 0

    @responses.activate
    def test_products_error(self):
        responses.add(responses.GET,
            f"{CONST_BASE_URL}:{CONST_PORT}/api/objects/products",
            status=400)
        self.assertRaises(HTTPError, self.gdm.products)

    def test_chores_valid(self):
        chores = self.gdm.chores().list
        assert isinstance(chores, tuple)
        assert len(chores) >=1
        for chore in chores:
            assert isinstance(chore, Chore)

    def test_locations_valid(self):
        locations = self.gdm.locations().list
        assert isinstance(locations, tuple)
        assert len(locations) >=1
        for location in locations:
            assert isinstance(location, Location)

    def test_batteries_valid(self):
        batteries = self.gdm.batteries().list
        assert isinstance(batteries, tuple)
        assert len(batteries) >=1
        for battery in batteries:
            assert isinstance(battery, Battery)

    def test_shopping_list_items_valid(self):
        shopping_list_items = self.gdm.shopping_list().list
        assert isinstance(shopping_list_items, tuple)
        assert len(shopping_list_items) >=1
        for items in shopping_list_items:
            assert isinstance(items, ShoppingListItem)

    def test_shopping_lists_valid(self):
        shopping_lists = self.gdm.shopping_lists().list
        assert isinstance(shopping_lists, tuple)
        assert len(shopping_lists) >=1
        for shopping_list in shopping_lists:
            assert isinstance(shopping_list, ShoppingList)

    def test_add_product_valid(self):
        product_list = self.gdm.products()
        old_len = len(product_list.list)
        new_product = {}
        new_product['name'] = 'Test product'
        new_product['location_id'] = 1
        new_product['qu_id_purchase'] = 1
        new_product['qu_id_stock'] = 1
        new_product['qu_factor_purchase_to_stock'] = 1
        new_product_id = product_list.add(new_product)
        new_len = len(product_list.list)
        assert isinstance(new_product_id, int)
        assert new_len == old_len + 1

    def test_add_product_error(self):
        product_list = self.gdm.products()
        new_product = {}
        new_product['name'] = 'Test product'
        self.assertRaises(HTTPError, product_list.add, new_product)

    def test_edit_product_valid(self):
        fields = {}
        fields['name'] = 'Test'
        assert not self.gdm.products().list[-1].edit(fields)

    def test_edit_product_error(self):
        fields = {}
        fields['nam'] = 'Test'
        product = self.gdm.products().list[0]
        self.assertRaises(HTTPError, product.edit, fields)

    def test_product_delete_valid(self):
        product = self.gdm.products().list[-1]
        old_len = len(self.gdm.products().list)
        assert not product.delete()
        self.gdm.products().refresh()
        new_len = len(self.gdm.products().list)
        assert new_len == old_len - 1

    def test_product_delete_error(self):
        product = self.gdm.products().list[-1]
        product.delete()
        self.assertRaises(HTTPError, product.delete)

    def test_search_product_valid(self):
        products = self.gdm.products().search("Co")
        assert isinstance(products, tuple)
        assert len(products) >=1
        for product in products:
            assert isinstance(product, Product)

    def test_search_product_invalid_no_data(self):
        products = self.gdm.products().search("Toto")
        assert products is None

    @responses.activate
    def test_search_product_error(self):
        url = f"{CONST_BASE_URL}:{CONST_PORT}/api/objects/products"
        responses.add_passthru(url)
        responses.add(responses.GET,
            f"{url}/search/error",
            status=400)
        products = self.gdm.products()
        self.assertRaises(HTTPError, products.search, "error")

    def test_quantity_units_valid(self):
        quantity_units = self.gdm.quantity_units().list
        assert isinstance(quantity_units, tuple)
        assert len(quantity_units) >=1
        for quantity_unit in quantity_units:
            assert isinstance(quantity_unit, QuantityUnit)

    def test_tasks_valid(self):
        tasks = self.gdm.tasks().list
        assert isinstance(tasks, tuple)
        assert len(tasks) >=1
        for task in tasks:
            assert isinstance(task, Task)

    def test_task_categories_valid(self):
        task_categories = self.gdm.task_categories().list
        assert isinstance(task_categories, tuple)
        assert len(task_categories) >=1
        for task_category in task_categories:
            assert isinstance(task_category, TaskCategory)

    def test_product_groups_valid(self):
        product_groups = self.gdm.product_groups().list
        assert isinstance(product_groups, tuple)
        assert len(product_groups) >=1
        for product_group in product_groups:
            assert isinstance(product_group, ProductGroup)

    def test_quantity_unit_conversions_valid(self):
        quantity_unit_conversions = self.gdm.quantity_unit_conversions().list
        assert isinstance(quantity_unit_conversions, tuple)
        assert len(quantity_unit_conversions) >=1
        for quantity_unit_conversion in quantity_unit_conversions:
            assert isinstance(quantity_unit_conversion, QuantityUnitConversion)

    def test_equipment_valid(self):
        equipments = self.gdm.equipment().list
        assert isinstance(equipments, tuple)
        assert len(equipments) >=1
        for equipment in equipments:
            assert isinstance(equipment, Equipment)

    def test_userfields_valid(self):
        userfields = self.gdm.userfields().list
        assert isinstance(userfields, tuple)
        assert len(userfields) >=1
        for userfield in userfields:
            assert isinstance(userfield, Userfield)

    def test_userentities_valid(self):
        userentities = self.gdm.userentities().list
        assert isinstance(userentities, tuple)
        assert len(userentities) >=1
        for userentity in userentities:
            assert isinstance(userentity, UserEntity)

    def test_userobjects_valid(self):
        userobjects = self.gdm.userobjects().list
        assert isinstance(userobjects, tuple)
        assert len(userobjects) >=1
        for userobject in userobjects:
            assert isinstance(userobject, UserObject)

    def test_meal_plan_valid(self):
        userobjects = self.gdm.meal_plan().list
        assert isinstance(userobjects, tuple)
        assert len(userobjects) >=1
        for userobject in userobjects:
            assert isinstance(userobject, MealPlan)

    def test_recipes_valid(self):
        recipes = self.gdm.recipes().list
        assert isinstance(recipes, tuple)
        assert len(recipes) >=1
        for recipe in recipes:
            assert isinstance(recipe, Recipe)

    def test_recipes_pos_valid(self):
        recipes_pos = self.gdm.recipes_pos().list
        assert isinstance(recipes_pos, tuple)
        assert len(recipes_pos) >=1
        for recipe_pos in recipes_pos:
            assert isinstance(recipe_pos, RecipePos)

    @responses.activate
    def test_get_userfields_valid(self):
        base_url = f"{CONST_BASE_URL}:{CONST_PORT}/api"
        resp =  {
                "uf1": 0,
                "uf2": "string"
            }
        userfields_url = f"{base_url}/userfields/products/1"
        responses.add(responses.GET, userfields_url, json=resp, status=200)
        responses.add_passthru(f"{base_url}/objects/products")
        product = self.gdm.products().list[0]

        product_uf = product.get_userfields()

        assert product_uf['uf1'] == 0

    def test_get_userfields_invalid_no_data(self):
        assert not self.gdm.products().list[0].get_userfields()

    @responses.activate
    def test_set_userfields_valid(self):
        base_url = f"{CONST_BASE_URL}:{CONST_PORT}/api"
        responses.add_passthru(f"{base_url}/objects/products")
        product = self.gdm.products().list[0]
        userfields_url = f"{base_url}/userfields/products/1"
        responses.add(responses.PUT, userfields_url, status=204)
        assert not product.set_userfields("auserfield", "value")

    @responses.activate
    def test_set_userfields_error(self):
        base_url = f"{CONST_BASE_URL}:{CONST_PORT}/api"
        responses.add_passthru(f"{base_url}/objects/products")
        product = self.gdm.products().list[0]
        userfields_url = f"{base_url}/userfields/products/1"
        responses.add(responses.PUT, userfields_url, status=400)
        self.assertRaises(HTTPError, product.set_userfields, "auserfield", "value")
