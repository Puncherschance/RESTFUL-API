import random
from random import randint
import string
import logging
from api import *
from env import Env


@pytest.fixture()
def api():
    api = Api()
    return api

@pytest.fixture()
def log():
    logging.info("Starting test!")
    yield
    logging.info(f"Status Code = {pytest.shared.status_code}")
    logging.info(pytest.shared.text)

@pytest.fixture()
def prereq_obj_id():
    api = Api()
    generated_data = api.dict_to_json(
                      {"name": ''.join(random.choices(string.ascii_letters, k=10)),
                       "data":
                           {"year": randint(2000,2023),
                            "price": randint(1000, 2000),
                            "CPU model": ''.join(random.choices(string.ascii_letters, k=5)),
                            "Hard disk size": str(randint(1, 10))+" TB"}
                       })
    res = api.send_post_request(Env.url, generated_data)
    return "/"+eval(res.text)["id"]

@pytest.fixture()
def generate_full_data():
    api = Api()
    generated_data = api.dict_to_json(
                      {"name": ''.join(random.choices(string.ascii_letters, k=10)),
                       "data":
                           {"year": randint(2000,2023),
                            "price": randint(1000, 2000),
                            "CPU model": ''.join(random.choices(string.ascii_letters, k=5)),
                            "Hard disk size": str(randint(1, 10))+"TB"}
                       })
    return generated_data

@pytest.fixture()
def generate_part_data():
    api = Api()
    generated_data = api.dict_to_json({"name": ''.join(random.choices(string.ascii_letters, k=10))})
    return generated_data

