import pytest
from selenium import webdriver
from urls import URLs
from pages.main_page import MainPageObjects
from pages.order_page import OrderPageObjects
from pages.status_page import StatusPageObjects
from pages.dzen_page import DzenPageObjects

@pytest.fixture(scope='class')
def driver_class():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_function():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def setup(driver_class):
    main_page = MainPageObjects(driver_class)
    driver_class.get(URLs.BASE_URL)
    main_page.wait_for_load_header()
    main_page.accept_cookies()
    main_page.scroll_to_questions()
    return main_page


@pytest.fixture(scope='function')
def main_page(driver_function):
    main_page = MainPageObjects(driver_function)
    driver_function.get(URLs.BASE_URL)
    main_page.wait_for_load_header()
    main_page.accept_cookies()
    return main_page

@pytest.fixture(scope='function')
def order_page(driver_function):
    return OrderPageObjects(driver_function)

@pytest.fixture(scope='function')
def status_page(driver_function):
    return StatusPageObjects(driver_function)

@pytest.fixture(scope='function')
def dzen_page(driver_function):
    return DzenPageObjects(driver_function)

