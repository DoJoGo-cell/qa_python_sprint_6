import allure
import pytest
from pages.main_page import MainPageObjects

class TestDropdownList:

    @allure.title('Проверка появления ответа из выпадающего списка "Вопросы о важном" при нажатии на вопрос №{number}')
    @allure.description('На странице скролим до вопроса с необходимым номером и кликаем на него, а затем проверяем что необходимый ответ с тем же номером появился')
    @pytest.mark.parametrize("number", [1,2,3,4,5,6,7,8])
    def test_question_and_answer(self, number, setup: MainPageObjects):
        main_page = setup

        main_page.click_questions(number)
        assert main_page.wait_for_answers(number)
    

    