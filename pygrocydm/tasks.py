from .grocy_api_client import GrocyApiClient
from .utils import parse_int, parse_bool, parse_float, parse_date
from typing import List, Tuple
import json
from datetime import datetime
from tzlocal import get_localzone
import pytz


TASKS_ENDPOINT = 'tasks'


class Task():
    def __init__(self, api_client: GrocyApiClient, parsed_json):
        self.__api_client = api_client
        self.__id = parse_int(parsed_json.get('id'))
        self.__endpoint = f"{TASKS_ENDPOINT}/{self.__id}"
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__due_date = parse_date(parsed_json.get('due_date', None))
        self.__done = parse_bool(parsed_json.get('done'), False)
        self.__done_timestamp = parse_date(
            parsed_json.get('done_timestamp', None))
        self.__category_id = parse_int(parsed_json.get('category_id'), None)
        self.__assigned_to_user_id = parse_int(
            parsed_json.get('assigned_to_user_id'))
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))

    def complete(self):
        endpoint = f"{self.__endpoint}/complete"
        self.__api_client.do_request("POST", endpoint)

    def undo(self):
        endpoint = f"{self.__endpoint}/undo"
        self.__api_client.do_request("POST", endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def due_date(self) -> datetime:
        return self.__due_date

    @property
    def done(self) -> bool:
        return self.__done

    @property
    def done_timestamp(self) -> datetime:
        return self.__done_timestamp

    @property
    def category_id(self) -> int:
        return self.__category_id

    @property
    def assigned_to_user_id(self) -> int:
        return self.__assigned_to_user_id

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp


class Tasks():
    def __init__(self, api_client: GrocyApiClient):
        self.__api_client = api_client
        self.__tasks_list = ()
        self.refresh()

    def refresh(self):
        endpoint = f"{TASKS_ENDPOINT}"
        parsed_json = self.__api_client.do_request("GET", endpoint)
        if parsed_json:
            self.__tasks_list = tuple([Task(self.__api_client, response)
                                                    for response in parsed_json])

    @property
    def tasks_list(self) -> Tuple[Task]:
        return self.__tasks_list
