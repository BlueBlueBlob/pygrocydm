import json
from datetime import datetime
from typing import Tuple

import requests

from .utils import parse_date, parse_int

DEFAULT_PORT_NUMBER = 9192


class GrocyApiClient():
    def __init__(
                self, base_url, api_key,
                port: int = DEFAULT_PORT_NUMBER, verify_ssl=True):
        self.__base_url = f"{base_url}:{port}/api/"
        self.__api_key = api_key
        self.__verify_ssl = verify_ssl
        if self.__api_key == "demo_mode":
            self.__headers = {"accept": "application/json"}
        else:
            self.__headers = {
                "accept": "application/json",
                "GROCY-API-KEY": api_key
            }

    def do_request(self, request_type: str, end_url: str, data=None):
        req_url = f"{self.__base_url}{end_url}"
        resp = None
        if request_type == "GET":
            resp = requests.get(
                req_url, verify=self.__verify_ssl, headers=self.__headers)
        if request_type == "POST":
            if isinstance(data, str):
                up_header = self.__headers.copy()
                up_header['accept'] = '*/*'
                up_header['Content-Type'] = 'application/json'
                resp = requests.post(
                    req_url, verify=self.__verify_ssl,
                    headers=up_header,
                    data=data)
            elif isinstance(data, dict):
                resp = requests.post(
                    req_url, verify=self.__verify_ssl,
                    headers=self.__headers,
                    data=data)
            else:
                resp = requests.post(
                    req_url, verify=self.__verify_ssl,
                    headers=self.__headers)
        if request_type == "PUT":
            if data:
                up_header = self.__headers.copy()
                up_header['accept'] = '*/*'
                up_header['Content-Type'] = 'application/json'
                resp = requests.put(
                    req_url, verify=self.__verify_ssl,
                    headers=up_header,
                    data=json.dumps(data))
        if request_type == "DELETE":
            resp = requests.delete(
                req_url, verify=self.__verify_ssl,
                headers=self.__headers)

        resp.raise_for_status()
        if len(resp.content) > 0:
            return resp.json()


class GrocyEntity():
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json: json):
        self.__api = api
        self.__parsed_json = parsed_json
        self.__id = parse_int(parsed_json.get('id'))
        self.__endpoint = f"{endpoint}/{self.__id}"
        self.__userfields_enpoint = self.__endpoint.replace(
            'objects', 'userfields')
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))

    def edit(self, data: dict):
        return self.__api.do_request("PUT", self.__endpoint, data)

    def delete(self):
        return self.__api.do_request("DELETE", self.__endpoint)

    def get_userfields(self):
        return self.__api.do_request("GET", self.__userfields_enpoint)

    def set_userfields(self, key, value):
        data = {
            key: value
        }
        return self.__api.do_request("PUT", self.__userfields_enpoint, data)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp


class GrocyEntityList():
    def __init__(self, api: GrocyApiClient, cls, endpoint: str):
        self.__api = api
        self.__cls = cls
        self.__endpoint = endpoint
        self.__list = ()
        self.refresh()

    def refresh(self):
        parsed_json = self.__api.do_request("GET", self.__endpoint)
        if parsed_json:
            self.__list = tuple([
                self.__cls(self.__api, self.__endpoint, response)
                for response in parsed_json
            ])

    def add(self, item: dict):
        resp = self.__api.do_request("POST", self.__endpoint, item)
        if resp:
            self.refresh()
            return parse_int(resp.get('created_object_id'))

    def search(self, search_str: str) -> Tuple[GrocyEntity]:
        endpoint = f"{self.__endpoint}/search/{search_str}"
        parsed_json = self.__api.do_request("GET", endpoint)
        if parsed_json:
            return tuple([
                self.__cls(self.__api, self.__endpoint, response)
                for response in parsed_json
            ])

    @property
    def list(self) -> Tuple[GrocyEntity]:
        return self.__list
