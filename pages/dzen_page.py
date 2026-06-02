from pages.base_page import BasePageObjects
from urls import URLs

class DzenPageObjects(BasePageObjects):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_dzen(self):
        self.wait_load_url(URLs.DZEN_URL)
