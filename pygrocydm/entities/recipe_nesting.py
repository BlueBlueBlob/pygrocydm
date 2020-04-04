from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_int

RECIPES_NESTINGS_ENDPOINT = 'objects/recipes_nestings'


class RecipeNesting(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__recipe_id = parse_int(parsed_json.get('recipe_id'))
        self.__includes_recipe_id = parse_int(
            parsed_json.get('includes_recipe_id'))
        self.__servings = parse_int(parsed_json.get('servings'))
        super().__init__(api, endpoint, parsed_json)

    @property
    def recipe_id(self) -> int:
        return self.__recipe_id

    @property
    def includes_recipe_id(self) -> int:
        return self.__includes_recipe_id

    @property
    def servings(self) -> int:
        return self.__servings
