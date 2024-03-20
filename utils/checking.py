import json
from requests import Response


'''Проверки ответов от сервера на ожидаймый результат'''
class Cheking_responses():

    '''Проверка на статус-код'''
    @staticmethod
    def check_status_code(response: Response, status_code):
        result = response.status_code
        assert result == status_code
        print(f'Статус код: {result}')


    '''Проверка на наличие обязательных полей'''
    @staticmethod
    def checking_required_fields(response: Response, expected_result):
        result = json.loads(response.text)
        assert result == expected_result
        print('ВCЕ ОБЯЗАТЕЛЬНЫЕ ПОЛЯ ПРИСУТСТВУЮТ В ОТВЕТЕ\n')