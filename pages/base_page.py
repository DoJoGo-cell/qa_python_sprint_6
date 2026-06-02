from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePageObjects:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def wait_element_visability(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_load_url(self, url):
        self.wait.until(expected_conditions.url_to_be(url))

    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click(self, locator):
        self.find(locator).click()

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_text(self, locator, data):
        element = self.find(locator)
        element.clear()
        element.send_keys(data)

    