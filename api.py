import requests
import allure
import pytest
import ast
from base_methods import BaseMethods


class Api(BaseMethods):

    @staticmethod
    def send_get_request(url):
        with allure.step("Send GET request to Server."):
            pytest.shared = requests.get(url)
            return pytest.shared

    @staticmethod
    def send_post_request(url, data):
        with allure.step("Send POST request to Server."):
            headers = {"Content-type": "application/json; charset=UTF-8"}
            pytest.shared = requests.post(url, data=data, headers=headers)
            return pytest.shared

    @staticmethod
    def send_put_request(url, data):
        with allure.step("Send PUT request to Server."):
            headers = {"Content-type": "application/json; charset=UTF-8"}
            pytest.shared = requests.put(url, data=data, headers=headers)
            return pytest.shared

    @staticmethod
    def send_patch_request(url, data):
        with allure.step("Send PATCH request to Server."):
            headers = {"Content-type": "application/json; charset=UTF-8"}
            return requests.patch(url, data=data, headers=headers)

    @staticmethod
    def send_delete_request(url):
        with allure.step("Send DELETE request to Server."):
            return requests.delete(url)

    def check_object_was_created(self, url, post_res, generate_data):
        with allure.step("Check that object data is matched with sent data."):
            post_data = self.convert_to_json(generate_data)
            post_id = self.eject_obj_id(post_res.text)
            get_res = self.send_get_request(url+"/"+post_id)
            get_data = self.eject_body(get_res)
            assert get_data == post_data, "Object data is not matched with sent data!"

    def check_object_was_updated(self, url, prereq_obj_id, data):
        with allure.step("Check that object data is matched with sent data."):
            get_res = self.send_get_request(url+prereq_obj_id)
            get_data = self.convert_to_json(get_res.text)
            del get_data["id"]
            del get_data["data"]
            put_data = eval(data)
            assert get_data == put_data, "Object data is not matched with sent data!"

    def validate_status_code(self, actual_code, expected_code):
        with allure.step("Validate received Status Code."):
            self.error_message = f"Status Code {actual_code} is not equal with {expected_code}!"
            assert self.compare_status_code(actual_code, expected_code), self.error_message

    def validate_schema(self, body):
        with allure.step("Validate received JSON Schema."):
            self.error_message = "Received JSON is not matched with schema!"
            assert self.compare_schema(body), self.error_message

    def validate_all_scheme(self, body):
        with allure.step("Validate received JSON Scheme."):
            self.error_message = "Received JSON is not matched with schema!"
            assert self.compare_scheme(body), self.error_message



