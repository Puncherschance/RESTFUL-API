import pytest
import allure
from env import Env
from api import *


@pytest.mark.GET
@allure.feature("GET Requests")
class TestGetRequests():


    @allure.story("Get list of all Objects")
    def test_get_list_of_all_objects(self, api, log):
        get_res = api.send_get_request(Env.url)
        api.validate_status_code(get_res.status_code, 200)
        api.validate_all_scheme(get_res.text)


    @allure.story("Get list of Objects by ID range")
    @pytest.mark.parametrize("range_id", ("?id=1&id=2&id=3", "?id=4&id=5"))
    def test_get_list_of_objects_by_id(self, api, range_id, log):
        get_res = api.send_get_request(Env.url+range_id)
        api.validate_status_code(get_res.status_code, 200)
        api.validate_all_scheme(get_res.text)


    @allure.story("Get single Object by ID")
    @pytest.mark.parametrize("obj_id", ("/1", "/2"))
    def test_get_single_object(self, api, obj_id, log):
        get_res = api.send_get_request(Env.url+obj_id)
        api.validate_status_code(get_res.status_code, 200)
        api.validate_schema(get_res.text)


@pytest.mark.POST
@allure.feature("POST requests")
class TestPostRequests:

    @allure.story("Post new Object")
    def test_post_new_object(self, api, generate_full_data, log):
        post_res = api.send_post_request(Env.url, generate_full_data)
        api.validate_status_code(post_res.status_code, 200)
        api.validate_schema(post_res.text)
        api.check_object_was_created(Env.url, post_res, generate_full_data)

@pytest.mark.PUT
@allure.feature("PUT Requests")
class TestPutRequests:

    @allure.story("PUT in Object")
    def test_put_in_object(self, api, prereq_obj_id, generate_part_data, log):
        put_res = api.send_put_request(Env.url+prereq_obj_id, generate_part_data)
        api.validate_status_code(put_res.status_code, 200)
        api.validate_schema(put_res.text)
        api.check_object_was_updated(Env.url, prereq_obj_id, generate_part_data)


@pytest.mark.PATCH
@allure.feature("PATCH Requests")
class TestPatchRequests:

    @allure.story("PATCH Object")
    @pytest.mark.parametrize("post_id", ("1", "2", "3", "4", "5"))
    def test_patch_post(self, api, post_id, write_log):
        patched_title = api.patch_title()
        res = api.send_patch_request(Env.url+post_id, data=patched_title)
        api.validate_status_code(res, 200)
        api.validate_schema(res)
        write_log(res)


@pytest.mark.DELETE
@allure.feature("DELETE Requests")
class TestDeleteRequests:

    @allure.story("DELETE the specific Post")
    @pytest.mark.parametrize("post_id", ("1", "2", "3", "4", "5"))
    def test_delete_post(self, api, post_id, write_log):
        res = api.send_delete_request(Env.url+post_id)
        api.validate_status_code(res, 200)
        write_log(res)
