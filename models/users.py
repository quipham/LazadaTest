from hamcrest import *
from helpers.request_helpers import RequestHelpers
import environment_constants as ec


def get_list_user(endpoint):
    response = RequestHelpers.send_get_request(endpoint)
    return response


def search_with_username(endpoint, user_name):
    response = RequestHelpers.send_get_request(endpoint, user_name)
    return response


def create_new_user(endpoint, user_information):
    response = RequestHelpers.send_post_request(endpoint, user_information)
    return response


def update_user(endpoint, user_id, user_information):
    endpoint = endpoint + user_id
    response = RequestHelpers.send_put_request(endpoint, user_information)
    return response


def delete_user_with_id(endpoint, user_id):
    response = RequestHelpers.send_delete_request(endpoint, user_id)
    return response


def verify_user_information_match(response, name, email, website):
    assert_that(name, equal_to(response['name']))
    assert_that(email, equal_to(response['email']))
    assert_that(website, equal_to(response['website']))


def verify_user_search_result_is_empty(result):
    assert_that(result, is_('[]'))


def verify_successful_response(response):
    assert_that(response.status_code, is_in(ec.SUCCES_STATUS_CODE))


def verify_page_not_found_response(response):
    assert_that(response.status_code, is_in(ec.PAGE_NOT_FOUND_STATUS_CODE))


def verify_bad_request_response(response):
    assert_that(response.status_code, is_in(ec.BAD_REQUEST_STATUS_CODE))
