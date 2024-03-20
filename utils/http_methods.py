import allure
import requests
from utils.logger import Logger

class Http_methods():
    '''Http методы'''

    headers = {'Content-Type':'application/json'}
    cookies = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.add_request_log(url, 'GET')
            result_get = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response_log(result_get)
            return result_get

    @staticmethod
    def post(url, body):
        with allure.step('POST'):
            Logger.add_request_log(url, 'POST')
            result_post = requests.post(url,json=body,headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response_log(result_post)
            return result_post

    @staticmethod
    def put(url, body):
        with allure.step('PUT'):
            Logger.add_request_log(url, 'PUT')
            result_put = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response_log(result_put)
            return result_put

    @staticmethod
    def delete(url, body):
        with allure.step('DELETE'):
            Logger.add_request_log(url, 'DELETE')
            result_delete = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response_log(result_delete)
            return result_delete
