import time
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageObjects

class MainPageObjects(BasePageObjects):

    def __init__(self, driver):
        super().__init__(driver)

        self.questions = {
            1: MainPageLocators.QUESTION_ONE,
            2: MainPageLocators.QUESTION_TWO,
            3: MainPageLocators.QUESTION_THREE,
            4: MainPageLocators.QUESTION_FOUR,
            5: MainPageLocators.QUESTION_FIVE,
            6: MainPageLocators.QUESTION_SIX,
            7: MainPageLocators.QUESTION_SEVEN,
            8: MainPageLocators.QUESTION_EIGHT,
        }
        self.answers = {
            1: MainPageLocators.ANSWER_ONE,
            2: MainPageLocators.ANSWER_TWO,
            3: MainPageLocators.ANSWER_THREE,
            4: MainPageLocators.ANSWER_FOUR,
            5: MainPageLocators.ANSWER_FIVE,
            6: MainPageLocators.ANSWER_SIX,
            7: MainPageLocators.ANSWER_SEVEN,
            8: MainPageLocators.ANSWER_EIGHT,
        }

    def accept_cookies(self):
        self.click(MainPageLocators.BUTTON_ACCEPT_COOKIES)
        

    def wait_for_load_header(self):
        self.wait_element_visability(MainPageLocators.MAIN_PAGE_HEADER)

    def scroll_to_questions(self):
        self.scroll_to(self.questions[1])
        time.sleep(1)


    def click_questions(self, num):
        self.click(self.questions[num])

    def wait_for_answers(self, num):
        time.sleep(1)
        self.wait_element_visability(self.answers[num])
        return True

    
    def click_order_button_above(self):
        self.click(MainPageLocators.BUTTON_ORDER_ABOVE)


    def scroll_to_order_button_below(self):
        self.scroll_to(MainPageLocators.BUTTON_ORDER_BELOW)

    def click_order_button_below(self):
        self.click(MainPageLocators.BUTTON_ORDER_BELOW)


    def click_header_logo_yandex(self):
        self.click(MainPageLocators.HEADER_LOGO_YANDEX)
        time.sleep(1)
        self.switch_to_new_window()