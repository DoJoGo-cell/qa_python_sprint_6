import allure
import pytest
from selenium import webdriver
from urls import URLs
from pages.main_page import MainPageObjects

class TestDropdownList:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.main_page = MainPageObjects(cls.driver)
        cls.driver.get(URLs.BASE_URL)
        cls.main_page.wait_for_load_header()
        cls.main_page.accept_cookies()
        cls.main_page.scroll_to_questions()

    @allure.title('Проверка появления ответа из выпадающего списка "Вопросы о важном" при нажатии на вопрос №{number}')
    @allure.description('На странице скролим до вопроса с необходимым номером и кликаем на него, а затем проверяем что необходимый ответ с тем же номером появился')
    @pytest.mark.parametrize("number", [1,2,3,4,5,6,7,8])
    def test_question_and_answer(self, number):
        self.main_page.click_questions(number)
        assert self.main_page.wait_for_answers(number)
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    