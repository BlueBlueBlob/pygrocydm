from .grocy_api_client import GrocyApiClient, GrocyEntity

EQUIPMENT_ENDPOINT = 'objects/equipment'


class Equipment(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__instruction_manual_file_name = parsed_json.get(
            'instruction_manual_file_name', None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def instruction_manual_file_name(self) -> str:
        return self.__instruction_manual_file_name
