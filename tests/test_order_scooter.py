import allure
import pytest
from selenium import webdriver
from urls import URLs
from pages.main_page import MainPageObjects
from pages.order_page import OrderPageObjects
from pages.status_page import StatusPageObjects
from pages.dzen_page import DzenPageObjects

@allure.feature('Заказ самоката')
@allure.story('Оформление заказа')
class TestOrderScooter:

    driver = None

    def setup_method(self):
            self.driver = webdriver.Firefox()

            self.main_page = MainPageObjects(self.driver)
            self.order_page = OrderPageObjects(self.driver)
            self.status_page = StatusPageObjects(self.driver)
            self.dzen_page = DzenPageObjects(self.driver)

            self.driver.get(URLs.BASE_URL)
            self.main_page.wait_for_load_header()

            self.main_page.accept_cookies()

    @allure.title('Заказ самоката через ВЕРХНЮЮ/НИЖНЮЮ кнопку "Заказать"')
    @allure.description('Тест проверяет полный цикл заказа самоката через ВЕРХНЮЮ и НИЖНЮЮ кнопку соответственно')
    @pytest.mark.parametrize('data_set_function', ['first_data_set', 'second_data_set'])
    def test_ordering_by_clicking_button(self, data_set_function):
        with allure.step('Переход к форме оформления заказа'):
            self.main_page.click_order_button_above()
            self.order_page.wait_for_load_first_header()

        with allure.step('Заполнение первой части формы оформления заказа (обязательными данными)'):
            getattr(self.order_page, data_set_function)()
            self.order_page.select_metro_station()
            self.order_page.check_is_selected_metro_station()

        with allure.step('Переход на вторую часть формы оформления'):
            self.order_page.click_button_next()
            self.order_page.wait_for_load_second_header()

        with allure.step('Заполнение второй части формы оформления заказа (обязательными данными)'):
            self.order_page.select_date()
            self.order_page.check_is_selected_date()
            self.order_page.select_rental_period()
            self.order_page.check_is_selected_rental_period()

        with allure.step('Завершение оформления заказа'):
            self.order_page.click_button_order()
            self.order_page.wait_for_load_confirm_window_header()

        with allure.step('Подтверждение заказа'):
            self.order_page.click_button_confirm()
            self.order_page.wait_for_load_completed_order_window_header()

        with allure.step('Переход на страницу статуса заказа'):
            self.order_page.click_button_check_status()
            self.status_page.wait_for_load_status_page()

        with allure.step('Переход на главную страницу Яндекс Самокат'):
            self.status_page.click_header_logo_scooter()
            self.main_page.wait_for_load_header()

        with allure.step('Переход на страницу Яндекс Дзен'):
            self.main_page.click_header_logo_yandex()
            self.dzen_page.wait_for_load_dzen()

        with allure.step('Проверка текущего URL'):
            assert self.driver.current_url == URLs.DZEN_URL

    def teardown_method(self):
            self.driver.quit()