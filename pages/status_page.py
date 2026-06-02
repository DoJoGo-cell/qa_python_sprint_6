import time
from locators.status_page_locators import StatusPageLocators
from pages.base_page import BasePageObjects

class StatusPageObjects(BasePageObjects):

    def __init__(self, driver):
        super().__init__(driver)


    def wait_for_load_status_page(self):
        time.sleep(2)
        self.wait_element_visability(StatusPageLocators.ORDER_INFO)

    def click_header_logo_scooter(self):
        self.click(StatusPageLocators.HEADER_LOGO_SCOOTER)