from .grocy_api_client import GrocyApiClient, GrocyEntity

QUANTITY_UNITS_ENDPOINT = 'objects/quantity_units'


class QuantityUnit(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__name_plural = parsed_json.get('name_plural')
        self.__description = parsed_json.get('description', None)
        self.__plural_forms = parsed_json.get('plural_forms', None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def name_plural(self) -> str:
        return self.__name_plural

    @property
    def plural_forms(self) -> str:
        return self.__plural_forms

    @property
    def description(self) -> str:
        return self.__description
