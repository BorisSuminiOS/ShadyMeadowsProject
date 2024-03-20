from utils.api_shady_meadows import Api_SM
from utils.checking import Cheking_responses
import json
import allure


@allure.epic('Тестирование сайта, отель "Shady Meadows" ')
class Test_Shady_Meadows():


    @allure.description('Тест отправки письма сотрудникам отеля')
    def test_send_msg(self):
        name = 'Борис'
        email = 'mtk26@bk.ru'
        phone = '89888486536'
        subject = 'Бронирование номера'
        description = 'Здравствуйте, планируем бронировать номер вашего отеля. Предоставьте пожалуйста прайс'
        result_test = Api_SM.send_msg(name, email, phone, subject, description)
        Cheking_responses.check_status_code(result_test, 201)
        check_info = json.loads(result_test.text)
        Cheking_responses.checking_required_fields(result_test, check_info)

    @allure.description('Тест бронирования комнаты')
    def test_booking_room(self):
        date_checkin = '2025-06-01'         # Если на эти даты уже бронировали номер, сервер вернет 409 ошибку и тест не пройдет
        date_checkout = '2025-06-09'
        firstname = 'Борис'
        lastname = 'Сумин'
        email = 'mtk26@bk.ru'
        phone = '89888486536'
        result_test = Api_SM.booking_room(date_checkin,date_checkout,firstname,lastname,email,phone)
        Cheking_responses.check_status_code(result_test, 201)
        check_info = json.loads(result_test.text)
        Cheking_responses.checking_required_fields(result_test, check_info)

    @allure.description('Тестирование полей на пустое значение')
    def test_negative_send_msg(self):
        result = Api_SM.negative_checking_fields()
        Cheking_responses.check_status_code(result, 400)
