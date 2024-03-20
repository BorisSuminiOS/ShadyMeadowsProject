import json
from utils.checking import Cheking_responses
from utils.http_methods import Http_methods

base_url = 'https://automationintesting.online'

'''Методы для отправки писем и бронирования номера в отеле'''
class Api_SM():

    '''Отправка письма в отель'''
    @staticmethod
    def send_msg(name, email, phone, subject, description):
        body_post = {"name": name,
                     "email": email,
                     "phone": phone,
                     "subject": subject,
                     "description": description
                     }
        resource_post = '/message/'
        url_post = base_url + resource_post
        result_post = Http_methods.post(url_post, body_post)
        print(f'ОТВЕТ ОТ СЕРВЕРА: {result_post.text}')
        return result_post

    @staticmethod
    def booking_room(date_checkin, date_checkout,firstname,lastname, email, phone):
        body_post = {
            "bookingdates": {"checkin":date_checkin,"checkout":date_checkout},
            "depositpaid": False,
            "firstname":firstname,
            "lastname":lastname,
            "roomid":1,
            "email":email,
            "phone":phone
            }

        resource_post = '/booking/'
        url_post = base_url + resource_post
        result_post = Http_methods.post(url_post, body_post)
        print(f'ОТВЕТ ОТ СЕРВЕРА: {result_post.text}')
        return result_post

    @staticmethod
    def negative_checking_fields():
        '''Проверка каждого поля, на пустое значение'''
        body_post = {"name": 'Борис',
                     "email": 'mtk26@bk.ru',
                     "phone": '89888486536',
                     "subject": 'Бронирование номера',
                     "description": 'Здравствуйте, планируем бронировать номер вашего отеля. Предоставьте пожалуйста прайс'
                     }
        for i in body_post.keys():
            body_post[i] = ''

            resource_post = '/message/'
            url_post = base_url + resource_post
            result_post = Http_methods.post(url_post, body_post)
            fields = json.loads(result_post.text)
            print(f'ТЕСТИРОВАНИЕ ПОЛЯ {i} НА ПУСТОЕ ЗНАЧЕНИЕ\nСТАТУС КОД: {result_post.status_code}\nОТВЕТ ОТ СЕРВЕРА: {result_post.text}')
            Cheking_responses.checking_required_fields(result_post, fields)
        return result_post