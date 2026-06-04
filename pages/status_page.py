import allure
from locators.status_page_locators import StatusPageLocators
from pages.base_page import BasePageObjects

class StatusPageObjects(BasePageObjects):

    @allure.step('Ожидание загрузки страницы статуса заказа')
    def wait_for_load_status_page(self):
        self.wait_element_visability(StatusPageLocators.ORDER_INFO)
        return True

    @allure.step('Нажатие на логотип "Самокат" на странице статуса заказа')
    def click_header_logo_scooter(self):
        self.click(StatusPageLocators.HEADER_LOGO_SCOOTER)