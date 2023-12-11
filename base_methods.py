import os.path
import json
import logging
from jsonschema import validate
from config import BASE_DIR



class BaseMethods():

    def compare_status_code(self, actual_code, expected_code):
        try:
            assert actual_code == expected_code
            return True
        except Exception:
            logging.exception(self.error_message)
            return False

    def compare_schema(self, body):
        expected_schema = self.load_schema("schema.json")
        body = self.convert_to_json(body)
        try:
            validate(body, expected_schema)
            return True
        except Exception:
            logging.exception(self.error_message)
            return False
    def compare_scheme(self, body):
        expected_schema = self.load_schema("schema.json")
        body = self.convert_to_json(body)
        try:
            for i in body:
                validate(i, expected_schema)
                return True
        except Exception:
            logging.exception(self.error_message)
            return False

    def load_schema(self, file_name):
        path = os.path.join(BASE_DIR, 'scheme', file_name)
        with open(path) as file:
            return json.loads(file.read())

    def convert_to_json(self, data):
        return json.loads(data)

    @staticmethod
    def dict_to_json(dict):
        return json.dumps(dict)

    def eject_obj_id(self, data):
        return eval(data)["id"]

    def eject_body(self, data):
        data = eval(data.text)
        del data["id"]
        return data


    @staticmethod
    def patch_title():
        return json.dumps({"title": "PATCHED!"})






