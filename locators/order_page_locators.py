from selenium.webdriver.common.by import By

class FirstFormSection:

    #Заголовок первой секции:
    ORDER_PAGE_HEADER = (By.XPATH, '//div[text()="Для кого самокат"]')

    #Логотип Самокат
    HEADER_LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')

    #Кнопка принятия Куки:
    BUTTON_ACCEPT_COOKIES = (By.XPATH, '//button[@id="rcc-confirm-button"]')

    #Форма заказа первой секции:
    INPUT_FIRST_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')

    INPUT_SECOND_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')

    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')

    INPUT_PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    METRO_DROPDOWN_LIST_HIDDEN = (By.XPATH, '//input[@class="select-search__input"]')

    METRO_DROPDOWN_LIST_ELEMENT_BUTTON = (By.XPATH, '//li[@class="select-search__row"]/button[@value="1"]')

    #Кнопка перехода во вторую секцию
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[text()="Далее"]')

class SecondFormSection:

    #Заголовок второй секции:
    ORDER_PAGE_HEADER = (By.XPATH, '//div[text()="Про аренду"]')

    #Форма заказа второй секции:
    DATE_LIST_HIDDEN = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')

    DATE_LIST_REVEALED = (By.CLASS_NAME, 'react-datepicker__tab-loop')

    DAY_IS_NOT_SELECTED = (By.XPATH, '//div[@tabindex="-1" and text()="25"]')

    DAY_IS_SELECTED = (By.XPATH, '//input[contains(@value, "25.")]')

    RENTAL_PERIOD_LIST_HIDDEN = (By.XPATH, '//span[@class="Dropdown-arrow"]')

    RENTAL_PERIOD_IS_NOT_SELECTED = (By.XPATH, '//div[@class="Dropdown-menu"]/div[text()="двое суток"]')

    RENTAL_PERIOD_IS_SELECTED = (By.XPATH, '//div[contains(text(), "двое суток")]')

    #Кнопка заказа:
    BUTTON_ORDER = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')

class OrderConfirmationWindow:

    #Заголовок окна:
    WINDOW_HEADER = (By.XPATH, '//div[contains(text(), "Хотите оформить заказ?")]')

    #Кнопка подтверждения заказа:
    BUTTON_CONFIRM = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]')

class OrderIsCompletedWindow:

    #Заголовок окна:
    ORDER_NUMBER = (By.XPATH, '//div[@class="Order_Text__2broi"]')

    #Кнопка проверки статуса заказа
    BUTTON_CHECK_STATUS = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[text()="Посмотреть статус"]')







