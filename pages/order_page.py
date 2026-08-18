import allure
from locators.order_page_locators import FirstFormSection, SecondFormSection, OrderConfirmationWindow, OrderIsCompletedWindow
from pages.base_page import BasePageObjects


class OrderPageObjects(BasePageObjects):

    @allure.step('Нажатие на логотип "Самокат" на странице оформления заказа')
    def click_header_logo_scooter(self):
        self.click(FirstFormSection.HEADER_LOGO_SCOOTER)

    @allure.step('Принятие файлов cookie')
    def accept_cookies(self):
        self.click(FirstFormSection.BUTTON_ACCEPT_COOKIES)

    @allure.step('Ожидание загрузки заголовка первой части формы оформления заказа')
    def wait_for_load_first_header(self):
        self.wait_element_visability(FirstFormSection.ORDER_PAGE_HEADER)

    @allure.step('Ввод в первую секцию формы оформления следующих данных: Имя, Фамилия, Адресс, Номер телефона')
    def fill_first_form_section(self, data: dict):
        self.send_text(FirstFormSection.INPUT_FIRST_NAME, data['FIRST_NAME'])
        self.send_text(FirstFormSection.INPUT_SECOND_NAME, data['SECOND_NAME'])
        self.send_text(FirstFormSection.INPUT_ADDRESS, data['ADDRESS'])
        self.send_text(FirstFormSection.INPUT_PHONE, data['PHONE_NUMBER'])

    @allure.step('Выбор станции метро')
    def select_metro_station(self):
        self.click(FirstFormSection.METRO_DROPDOWN_LIST_HIDDEN)
        self.click(FirstFormSection.METRO_DROPDOWN_LIST_ELEMENT_BUTTON)

    @allure.step('Проверка появлении выбранной станции метро в форме')
    def check_is_selected_metro_station(self):
        element = self.find(FirstFormSection.METRO_DROPDOWN_LIST_HIDDEN)
        assert element.get_attribute('value') is not None

    @allure.step('Нажатие на кнопку "Далее" под первой частью формы оформления заказа')
    def click_button_next(self):
        self.click(FirstFormSection.BUTTON_NEXT)

    @allure.step('Ожидание загрузки заголовка второй части формы оформления заказа')
    def wait_for_load_second_header(self):
        self.wait_element_visability(SecondFormSection.ORDER_PAGE_HEADER)

    @allure.step('Выбор даты начала аренды')
    def select_date(self):
        self.click(SecondFormSection.DATE_LIST_HIDDEN)
        self.click(SecondFormSection.DAY_IS_NOT_SELECTED)

    @allure.step('Проверка появлении выбранной даты в форме')
    def check_is_selected_date(self):
        element = self.find(SecondFormSection.DAY_IS_SELECTED)
        assert "25." in element.get_attribute('value') 

    @allure.step('Выбор периода аренды')
    def select_rental_period(self):
        self.click(SecondFormSection.RENTAL_PERIOD_LIST_HIDDEN)
        self.click(SecondFormSection.RENTAL_PERIOD_IS_NOT_SELECTED)

    @allure.step('Проверка появлении выбранного периода в форме')
    def check_is_selected_rental_period(self):
        element = self.find(SecondFormSection.RENTAL_PERIOD_IS_SELECTED)
        assert element.text == "двое суток"

    @allure.step('Нажатие на кнопку "Заказать" под второй частью формы оформления заказа')
    def click_button_order(self):
        self.click(SecondFormSection.BUTTON_ORDER)

    @allure.step('Ожидание появления заголовка окна подтверждения заказа')
    def wait_for_load_confirm_window_header(self):
        self.wait_element_visability(OrderConfirmationWindow.WINDOW_HEADER)

    @allure.step('Нажатие на кнопку "Да" в окне подтверждения заказа')
    def click_button_confirm(self):
        self.click(OrderConfirmationWindow.BUTTON_CONFIRM)

    @allure.step('Ожидание загрузки окна оформленного заказа')
    def wait_for_load_completed_order_window(self):
        self.wait_text_matches(OrderIsCompletedWindow.ORDER_NUMBER, r'Номер заказа: \d+')

    @allure.step('Нажатие на кнопку "Посмотреть статус" в окне оформленного заказа')
    def click_button_check_status(self):
        self.click(OrderIsCompletedWindow.BUTTON_CHECK_STATUS)


