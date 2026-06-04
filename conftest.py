import pytest
from selenium import webdriver
from urls import URLs
from pages.main_page import MainPageObjects
from pages.order_page import OrderPageObjects

@pytest.fixture(scope='class')
def first_setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URLs.BASE_URL)

    main_page = MainPageObjects(driver)
    main_page.wait_for_load_header()
    main_page.accept_cookies()
    main_page.scroll_to_questions()

    yield driver
    
    driver.quit()

@pytest.fixture(scope='function')
def second_setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URLs.BASE_URL)

    main_page = MainPageObjects(driver)
    main_page.wait_for_load_header()
    main_page.accept_cookies()

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def third_setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URLs.ORDER_URL)

    order_page= OrderPageObjects(driver)
    order_page.wait_for_load_first_header()
    order_page.accept_cookies()

    yield driver

    driver.quit()