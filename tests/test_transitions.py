import allure
from urls import URLs
from pages.main_page import MainPageObjects
from pages.order_page import OrderPageObjects
from pages.dzen_page import DzenPageObjects

@allure.feature('Переходы между страницами')
@allure.story('Переход по логотипам "Самокат" и "Яндекс"')
class TestTransitions:

    @allure.title('Проверка перехода на главную страницу Яндекс Самокат')
    @allure.description('Тест проверяет переход на главную страницу сервиса нажатием по логотипу "Самокат" на странице оформления заказа')
    def test_transition_to_main_page(self, third_setup):
        order_page = OrderPageObjects(third_setup)
        main_page = MainPageObjects(third_setup)

        with allure.step('Переход на главную страницу Яндекс Самокат'):
            order_page.click_header_logo_scooter()
            main_page.wait_for_load_header()

        with allure.step('Проверка текущего URL'):
            assert main_page.driver.current_url == URLs.BASE_URL

    @allure.title('Проверка перехода на страницу Яндекс Дзен')
    @allure.description('Тест проверяет переход на страницу Яндекс Дзен нажатием по логотипу "Яндекс" на главной странице сервиса')
    def test_transition_to_dzen_page(self, second_setup):
        dzen_page= DzenPageObjects(second_setup)
        main_page = MainPageObjects(second_setup)

        with allure.step('Переход на страницу Яндекс Дзен'):
            main_page.click_header_logo_yandex()
            dzen_page.wait_for_load_dzen()

        with allure.step('Проверка текущего URL'):
            assert dzen_page.driver.current_url == URLs.DZEN_URL

