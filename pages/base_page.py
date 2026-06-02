import re
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePageObjects:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Получение элемента: {locator}')
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Ожидание видимости элемента: {locator}')
    def wait_element_visability(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание появления номера заказа')
    def wait_text_matches(self, locator, pattern):
        element = self.find(locator)
        self.wait.until(lambda _: bool(re.search(pattern, element.text)))

    @allure.step('Ожидание появления URL ссылки: {url}')
    def wait_load_url(self, url):
        self.wait.until(expected_conditions.url_to_be(url))

    @allure.step('Переход на последнюю открытую вкладку')
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step('Клик по элементу: {locator}')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Скрол до элемента: {locator}')
    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Отправка данных {data} в элемент: {locator}')
    def send_text(self, locator, data):
        element = self.find(locator)
        element.clear()
        element.send_keys(data)

    