from .grocy_api_client import GrocyApiClient
from .utils import parse_date

from datetime import date, datetime

SYSTEM_ENDPOINT = 'system'


class System():
    def __init__(self, api_client: GrocyApiClient):
        self.__api_client = api_client
        self.__versions()

    def __versions(self):
        endpoint = f"{SYSTEM_ENDPOINT}/info"
        parsed_json = self.__api_client.do_request("GET", endpoint)
        self.__grocy_version = parsed_json.get('grocy_version').get('Version')
        self.__grocy_release_date = parse_date(parsed_json.get('grocy_version').get('ReleaseDate')).date
        self.__php_version = parsed_json.get('php_version')
        self.__sqlite_version = parsed_json.get('sqlite_version')

    def db_changed_time(self) -> datetime:
        endpoint = f"{SYSTEM_ENDPOINT}/db-changed-time"
        parsed_json = self.__api_client.do_request("GET", endpoint)
        return parse_date(parsed_json.get('changed_time'))

    @property
    def grocy_version(self) -> str:
        return self.__grocy_version

    @property
    def grocy_release_date(self) -> date:
        return self.__grocy_release_date

    @property
    def php_version(self) -> str:
        return self.__php_version

    @property
    def sqlite_version(self) -> str:
        return self.__sqlite_version
 