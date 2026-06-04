import allure
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

    @allure.step('Принятие файлов cookie')
    def accept_cookies(self):
        self.click(MainPageLocators.BUTTON_ACCEPT_COOKIES)
        
    @allure.step('Ожидание загрузки заголовка главной страиницы')
    def wait_for_load_header(self):
        self.wait_element_visability(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step('Скрол до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        self.scroll_to(self.questions[1])

    @allure.step('Нажатие на вопрос №{num}')
    def click_questions(self, num):
        self.click(self.questions[num])

    @allure.step('Ожидание появления ответа на вопрос №{num}')
    def wait_for_answers(self, num):
        self.wait_element_visability(self.answers[num])
        return True

    @allure.step('Нажатие на кнопку "Заказать" в верхней части главной страницы')
    def click_order_button_above(self):
        self.click(MainPageLocators.BUTTON_ORDER_ABOVE)

    @allure.step('Скрол до кнопки "Заказать" в нижней части главной страницы')
    def scroll_to_order_button_below(self):
        self.scroll_to(MainPageLocators.BUTTON_ORDER_BELOW)

    @allure.step('Нажатие на кнопку "Заказать" в нижней части главной страницы')
    def click_order_button_below(self):
        self.click(MainPageLocators.BUTTON_ORDER_BELOW)

    @allure.step('Клик по логотипу Яндекса и переход в Дзен')
    def click_header_logo_yandex(self):
        self.click(MainPageLocators.HEADER_LOGO_YANDEX)
        self.switch_to_new_window()
