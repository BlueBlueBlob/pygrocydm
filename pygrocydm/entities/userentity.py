from pygrocydm.grocy_api_client import GrocyApiClient, GrocyEntity
from pygrocydm.utils import parse_bool

USERENTITIES_ENDPOINT = 'objects/userentities'


class UserEntity(GrocyEntity):
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json):
        self.__name = parsed_json.get('name')
        self.__caption = parsed_json.get('caption')
        self.__description = parsed_json.get('description', None)
        self.__show_in_sidebar_menu = parse_bool(
            parsed_json.get('show_in_sidebar_menu'), False)
        self.__icon_css_class = parsed_json.get('icon_css_class', None)
        super().__init__(api, endpoint, parsed_json)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def caption(self) -> str:
        return self.__caption

    @property
    def description(self) -> str:
        return self.__description

    @property
    def show_in_sidebar_menu(self) -> bool:
        return self.__show_in_sidebar_menu

    @property
    def icon_css_class(self) -> str:
        return self.__icon_css_class
