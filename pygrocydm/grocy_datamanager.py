from .entities.battery import BATTERIES_ENDPOINT, Battery
from .entities.chore import CHORES_ENDPOINT, Chore
from .entities.equipment import EQUIPMENT_ENDPOINT, Equipment
from .entities.location import LOCATION_ENDPOINT, Location
from .entities.meal_plan import MEAL_PLAN_ENDPOINT, MealPlan
from .entities.product import PRODUCTS_ENDPOINT, Product
from .entities.product_group import PRODUCT_GROUPS_ENDPOINT, ProductGroup
from .entities.quantity_unit import QUANTITY_UNITS_ENDPOINT, QuantityUnit
from .entities.quantity_unit_conversion import (QUANTITY_UNIT_CONVERTIONS_ENDPOINT,
                                                                                           QuantityUnitConversion)
from .entities.recipe import RECIPES_ENDPOINT, Recipe
from .entities.recipe_nesting import RECIPES_NESTINGS_ENDPOINT, RecipeNesting
from .entities.recipe_pos import RECIPES_POS_ENDPOINT, RecipePos
from .entities.shopping_list import (SHOPPING_LIST_ENDPOINT, SHOPPING_LISTS_ENDPOINT,
                                                                    ShoppingList, ShoppingListItem)
from .entities.task import TASKS_ENDPOINT, Task
from .entities.task_category import TASK_CATEGORIES_ENDPOINT, TaskCategory
from .entities.userentity import USERENTITIES_ENDPOINT, UserEntity
from .entities.userfield import USERFIELDS_ENDPOINT, Userfield
from .entities.userobject import USEROBJECTS_ENDPOINT, UserObject
from .grocy_api_client import GrocyApiClient, GrocyEntityList


class GrocyDataManager():
    def __init__(self, api_client: GrocyApiClient):
        self.__api_client = api_client

    def products(self) -> GrocyEntityList:
        cls = Product
        return GrocyEntityList(self.__api_client, cls, PRODUCTS_ENDPOINT)

    def chores(self) -> GrocyEntityList:
        cls = Chore
        return GrocyEntityList(self.__api_client, cls, CHORES_ENDPOINT)

    def locations(self) -> GrocyEntityList:
        cls = Location
        return GrocyEntityList(self.__api_client, cls, LOCATION_ENDPOINT)

    def batteries(self) -> GrocyEntityList:
        cls = Battery
        return GrocyEntityList(self.__api_client, cls, BATTERIES_ENDPOINT)

    def shopping_list(self) -> GrocyEntityList:
        cls = ShoppingListItem
        return GrocyEntityList(self.__api_client, cls, SHOPPING_LIST_ENDPOINT)

    def shopping_lists(self) -> GrocyEntityList:
        cls = ShoppingList
        return GrocyEntityList(self.__api_client, cls, SHOPPING_LISTS_ENDPOINT)

    def quantity_unit_conversions(self) -> GrocyEntityList:
        cls = QuantityUnitConversion
        return GrocyEntityList(
            self.__api_client, cls, QUANTITY_UNIT_CONVERTIONS_ENDPOINT)

    def quantity_units(self) -> GrocyEntityList:
        cls = QuantityUnit
        return GrocyEntityList(self.__api_client, cls, QUANTITY_UNITS_ENDPOINT)

    def tasks(self) -> GrocyEntityList:
        cls = Task
        return GrocyEntityList(self.__api_client, cls, TASKS_ENDPOINT)

    def task_categories(self) -> GrocyEntityList:
        cls = TaskCategory
        return GrocyEntityList(self.__api_client, cls, TASK_CATEGORIES_ENDPOINT)

    def product_groups(self) -> GrocyEntityList:
        cls = ProductGroup
        return GrocyEntityList(self.__api_client, cls, PRODUCT_GROUPS_ENDPOINT)

    def equipment(self) -> GrocyEntityList:
        cls = Equipment
        return GrocyEntityList(self.__api_client, cls, EQUIPMENT_ENDPOINT)

    def userfields(self) -> GrocyEntityList:
        cls = Userfield
        return GrocyEntityList(self.__api_client, cls, USERFIELDS_ENDPOINT)

    def userentities(self) -> GrocyEntityList:
        cls = UserEntity
        return GrocyEntityList(self.__api_client, cls, USERENTITIES_ENDPOINT)

    def userobjects(self) -> GrocyEntityList:
        cls = UserObject
        return GrocyEntityList(self.__api_client, cls, USEROBJECTS_ENDPOINT)

    def meal_plan(self) -> GrocyEntityList:
        cls = MealPlan
        return GrocyEntityList(self.__api_client, cls, MEAL_PLAN_ENDPOINT)

    def recipes(self) -> GrocyEntityList:
        cls = Recipe
        return GrocyEntityList(self.__api_client, cls, RECIPES_ENDPOINT)

    def recipes_pos(self) -> GrocyEntityList:
        cls = RecipePos
        return GrocyEntityList(self.__api_client, cls, RECIPES_POS_ENDPOINT)

    def recipes_nestings(self) -> GrocyEntityList:
        cls = RecipeNesting
        return GrocyEntityList(self.__api_client, cls, RECIPES_NESTINGS_ENDPOINT)
