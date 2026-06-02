import allure
from pages.base_page import BasePageObjects
from urls import URLs

class DzenPageObjects(BasePageObjects):

    @allure.step('Ожидание закгрузки URL Яндекс Дзен')
    def wait_for_load_dzen(self):
        self.wait_load_url(URLs.DZEN_URL)
