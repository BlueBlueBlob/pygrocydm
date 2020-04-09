from pygrocydm.grocy_api_client import DEFAULT_PORT_NUMBER, GrocyApiClient
from pygrocydm.grocy_datamanager import GrocyDataManager
from pygrocydm.recipes import Recipes
from pygrocydm.tasks import Tasks
from pygrocydm.system import System


class GrocyAPI():
    """ Main class """

    def __init__(
            self, base_url, api_key,
            port: int = DEFAULT_PORT_NUMBER,
            verify_ssl=True):
        """
        Constructor requiring base url and API key.
        Attributes:
            base_url: Grocy server url.
            api_key: Grocy API key.
        """
        self.__api_client = GrocyApiClient(base_url, api_key, port, verify_ssl)

    def generic_entities(self) -> GrocyDataManager:
        return GrocyDataManager(self.__api_client)

    def recipes(self) -> Recipes:
        return Recipes(self.__api_client)

    def tasks(self) -> Tasks:
        return Tasks(self.__api_client)

    def system(self) -> System:
        return System(self.__api_client)
