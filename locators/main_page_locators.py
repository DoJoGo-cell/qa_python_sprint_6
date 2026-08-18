from selenium.webdriver.common.by import By

class MainPageLocators:

    #Кнопка принятия Куки:
    BUTTON_ACCEPT_COOKIES = (By.XPATH, '//button[@id="rcc-confirm-button"]')

    #Логотип Яндекс:
    HEADER_LOGO_YANDEX = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')

    #Заголовок главной страницы:
    MAIN_PAGE_HEADER = (By.CLASS_NAME, 'Home_Header__iJKdX')

    #Кнопка заказа вверху страницы:
    BUTTON_ORDER_ABOVE = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')

    #Кнопка заказа снизу страницы:
    BUTTON_ORDER_BELOW = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')

    #Вопросы:
    QUESTION_ONE = (By.ID, 'accordion__heading-0')

    QUESTION_TWO = (By.ID, 'accordion__heading-1')

    QUESTION_THREE = (By.ID, 'accordion__heading-2')

    QUESTION_FOUR = (By.ID, 'accordion__heading-3')

    QUESTION_FIVE = (By.ID, 'accordion__heading-4')
    
    QUESTION_SIX = (By.ID, 'accordion__heading-5')
    
    QUESTION_SEVEN = (By.ID, 'accordion__heading-6')

    QUESTION_EIGHT = (By.ID, 'accordion__heading-7')

    #Ответы
    ANSWER_ONE = (By.ID, 'accordion__panel-0')

    ANSWER_TWO = (By.ID, 'accordion__panel-1')

    ANSWER_THREE = (By.ID, 'accordion__panel-2')

    ANSWER_FOUR = (By.ID, 'accordion__panel-3')

    ANSWER_FIVE = (By.ID, 'accordion__panel-4')

    ANSWER_SIX = (By.ID, 'accordion__panel-5')

    ANSWER_SEVEN = (By.ID, 'accordion__panel-6')

    ANSWER_EIGHT = (By.ID, 'accordion__panel-7')