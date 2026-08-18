import allure
from urls import URLs
from pages.main_page import MainPageObjects
from pages.order_page import OrderPageObjects
from pages.status_page import StatusPageObjects
from pages.dzen_page import DzenPageObjects
from data_for_order import Data

@allure.feature('Заказ самоката')
@allure.story('Оформление заказа')
class TestOrderScooter:

    @allure.title('Заказ самоката через ВЕРХНЮЮ кнопку "Заказать"')
    @allure.description('Тест проверяет полный цикл заказа самоката через ВЕРХНЮЮ кнопку')
    def test_ordering_by_clicking_button_above(self, second_setup):
        order_page = OrderPageObjects(second_setup)
        status_page = StatusPageObjects(second_setup)
        dzen_page = DzenPageObjects(second_setup)
        main_page = MainPageObjects(second_setup)

        with allure.step('Переход к форме оформления заказа через ВЕРХНЮЮ кнопку'):
            main_page.click_order_button_above()
            order_page.wait_for_load_first_header()

        with allure.step('Заполнение первой части формы оформления заказа (обязательными данными)'):
            order_page.fill_first_form_section(Data.First_data_set)
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

        with allure.step('Проверка загрузки страницы статуса заказа'):
            assert status_page.wait_for_load_status_page()


    @allure.title('Заказ самоката через НИЖНЮЮ кнопку "Заказать"')
    @allure.description('Тест проверяет полный цикл заказа самоката через НИЖНЮЮ кнопку')
    def test_ordering_by_clicking_button_below(self, second_setup):
        order_page = OrderPageObjects(second_setup)
        status_page = StatusPageObjects(second_setup)
        dzen_page = DzenPageObjects(second_setup)
        main_page = MainPageObjects(second_setup)

        with allure.step('Переход к форме оформления заказа через НИЖНЮЮ кнопку'):
            main_page.scroll_to_order_button_below()
            main_page.click_order_button_below()
            order_page.wait_for_load_first_header()

        with allure.step('Заполнение первой части формы оформления заказа (обязательными данными)'):
            order_page.fill_first_form_section(Data.Second_data_set)
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
            
        with allure.step('Проверка загрузки страницы статуса заказа'):
            assert status_page.wait_for_load_status_page()

