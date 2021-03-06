import environment_constants as ec
import requests


class RequestHelpers(object):
    # Because the test API server don't have the headers/Token/Session/Key then we don't need these param
    @staticmethod
    def send_get_request(end_point, data=""):
        url = ec.BASE_API_URL + end_point + data
        return requests.get(url)

    # Method to send PUT request to specific endpoint with data
    @staticmethod
    def send_put_request(end_point, data):
        url = ec.BASE_API_URL + end_point
        return requests.put(url, data=data)

    # Method to send POST request to specific endpoint with data
    @staticmethod
    def send_post_request(end_point, data):
        url = ec.BASE_API_URL + end_point
        return requests.post(url, data=data)

    # Method to send DELETE request to specific endpoint with data
    @staticmethod
    def send_delete_request(end_point, data):
        url = ec.BASE_API_URL + end_point + data
        return requests.delete(url)
