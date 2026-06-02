import allure
import pytest
from urls import URLs
from pages.main_page import MainPageObjects
from pages.order_page import OrderPageObjects
from pages.status_page import StatusPageObjects
from pages.dzen_page import DzenPageObjects
from data_for_order import Data

@allure.feature('Заказ самоката')
@allure.story('Оформление заказа')
class TestOrderScooter:

    @allure.title('Заказ самоката через ВЕРХНЮЮ/НИЖНЮЮ кнопку "Заказать"')
    @allure.description('Тест проверяет полный цикл заказа самоката через ВЕРХНЮЮ и НИЖНЮЮ кнопку соответственно')
    @pytest.mark.parametrize('data', [Data.First_data_set, Data.Second_data_set])
    def test_ordering_by_clicking_button(
            self, 
            data, 
            main_page: MainPageObjects,
            order_page: OrderPageObjects,
            status_page: StatusPageObjects,
            dzen_page: DzenPageObjects,
            ):

        with allure.step('Переход к форме оформления заказа'):
            main_page.click_order_button_above()
            order_page.wait_for_load_first_header()

        with allure.step('Заполнение первой части формы оформления заказа (обязательными данными)'):
            order_page.fill_first_form_section(data)
            order_page.select_metro_station()
            order_page.check_is_selected_metro_station()

        with allure.step('Переход на вторую часть формы оформления'):
            order_page.click_button_next()
            order_page.wait_for_load_second_header()

        with allure.step('Заполнение второй части формы оформления заказа (обязательными данными)'):
            order_page.select_date()
            order_page.check_is_selected_date()
            order_page.select_rental_period()
            order_page.check_is_selected_rental_period()

        with allure.step('Завершение оформления заказа'):
            order_page.click_button_order()
            order_page.wait_for_load_confirm_window_header()

        with allure.step('Подтверждение заказа'):
            order_page.click_button_confirm()
            order_page.wait_for_load_completed_order_window()

        with allure.step('Переход на страницу статуса заказа'):
            order_page.click_button_check_status()
            status_page.wait_for_load_status_page()

        with allure.step('Переход на главную страницу Яндекс Самокат'):
            status_page.click_header_logo_scooter()
            main_page.wait_for_load_header()

        with allure.step('Переход на страницу Яндекс Дзен'):
            main_page.click_header_logo_yandex()
            dzen_page.wait_for_load_dzen()

        with allure.step('Проверка текущего URL'):
            assert dzen_page.driver.current_url == URLs.DZEN_URL
