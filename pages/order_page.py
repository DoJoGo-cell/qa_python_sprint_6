import time
from locators.order_page_locators import FirstFormSection, SecondFormSection, OrderConfirmationWindow, OrderIsCompletedWindow
from pages.base_page import BasePageObjects
from data_for_order import Data

class OrderPageObjects(BasePageObjects):

    def __init__(self, driver):
        super().__init__(driver)


    def wait_for_load_first_header(self):
        self.wait_element_visability(FirstFormSection.ORDER_PAGE_HEADER)

    def first_data_set(self):
        self.send_text(FirstFormSection.INPUT_FIRST_NAME, Data.First_data_set['FIRST_NAME'])
        self.send_text(FirstFormSection.INPUT_SECOND_NAME, Data.First_data_set['SECOND_NAME'])
        self.send_text(FirstFormSection.INPUT_ADDRESS, Data.First_data_set['ADDRESS'])
        self.send_text(FirstFormSection.INPUT_PHONE, Data.First_data_set['PHONE_NUMBER'])

    def second_data_set(self):
        self.send_text(FirstFormSection.INPUT_FIRST_NAME, Data.Second_data_set['FIRST_NAME'])
        self.send_text(FirstFormSection.INPUT_SECOND_NAME, Data.Second_data_set['SECOND_NAME'])
        self.send_text(FirstFormSection.INPUT_ADDRESS, Data.Second_data_set['ADDRESS'])
        self.send_text(FirstFormSection.INPUT_PHONE, Data.Second_data_set['PHONE_NUMBER'])

    def select_metro_station(self):
        self.click(FirstFormSection.METRO_DROPDOWN_LIST_HIDDEN)
        time.sleep(1)
        self.click(FirstFormSection.METRO_DROPDOWN_LIST_ELEMENT_BUTTON)

    def check_is_selected_metro_station(self):
        element = self.find(FirstFormSection.METRO_DROPDOWN_LIST_HIDDEN)
        assert element.get_attribute('value') is not None

    def click_button_next(self):
        self.click(FirstFormSection.BUTTON_NEXT)

    def wait_for_load_second_header(self):
        self.wait_element_visability(SecondFormSection.ORDER_PAGE_HEADER)

    def select_date(self):
        self.click(SecondFormSection.DATE_LIST_HIDDEN)
        self.click(SecondFormSection.DAY_IS_NOT_SELECTED)

    def check_is_selected_date(self):
        element = self.find(SecondFormSection.DAY_IS_SELECTED)
        assert "25." in element.get_attribute('value') 

    def select_rental_period(self):
        self.click(SecondFormSection.RENTAL_PERIOD_LIST_HIDDEN)
        self.click(SecondFormSection.RENTAL_PERIOD_IS_NOT_SELECTED)

    def check_is_selected_rental_period(self):
        element = self.find(SecondFormSection.RENTAL_PERIOD_IS_SELECTED)
        assert element.text == "двое суток"

    def click_button_order(self):
        self.click(SecondFormSection.BUTTON_ORDER)

    def wait_for_load_confirm_window_header(self):
        self.wait_element_visability(OrderConfirmationWindow.WINDOW_HEADER)

    def click_button_confirm(self):
        self.click(OrderConfirmationWindow.BUTTON_CONFIRM)


    def wait_for_load_completed_order_window_header(self):
        time.sleep(2)
        self.wait_element_visability(OrderIsCompletedWindow.WINDOW_HEADER)

    def click_button_check_status(self):
        self.click(OrderIsCompletedWindow.BUTTON_CHECK_STATUS)


