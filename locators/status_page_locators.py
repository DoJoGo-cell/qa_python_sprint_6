from selenium.webdriver.common.by import By

class StatusPageLocators:

    #Кнопка отмены заказа:
    ORDER_INFO = (By.XPATH, '//div[contains(@class, "Track_OrderInfo")]//button[text()="Отменить заказ"]')

    #Логотип Самокат
    HEADER_LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')

    