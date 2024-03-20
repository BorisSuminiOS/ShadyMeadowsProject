import datetime
import os
from requests import Response

class Logger():


    file = f'logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log'

    @classmethod
    def creating_file_logs(cls, data: str):
        '''Создание и добавления файла для логов'''
        with open(cls.file, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)


    @classmethod
    def add_request_log(cls, url: str, method: str):
        '''Добавление всех все отправленных запросов в файл logs'''
        name_test = os.environ.get("PYTEST_CURRENT_TEST")

        data_to_add = '\n-----\n'
        data_to_add += f'Test: {name_test}\n'
        data_to_add += f'Time: {datetime.datetime.now()}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += '\n'

        cls.creating_file_logs(data_to_add)


    @classmethod
    def add_response_log(cls, response: Response):
        '''Добавление всех ответов от сервера в файл logs'''
        cookies = dict(response.cookies)
        headers = dict(response.headers)

        data_to_add = f'Status code: {response.status_code}\n'
        data_to_add += f'Status text: {response.text}\n'
        data_to_add += f'Response cookies: {cookies}\n'
        data_to_add += f'Response headers: {headers}\n'
        data_to_add += f'\n-----\n'

        cls.creating_file_logs(data_to_add)
