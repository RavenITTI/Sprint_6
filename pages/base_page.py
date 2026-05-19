import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import URLS

class BasePage:
 
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URLS.BASE_URL
    @allure.step("Открыть главный сайт")
    def open_site(self):
        return self.driver.get(self.base_url)
    
    
    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator, time=10):
        
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не найден по локатору: {locator}"
        )

    @allure.step("Ожидать, пока элемент станет кликабельным")
    def wait_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не стал кликабельным: {locator}"
        )
   
   
    @allure.step("Выполнить клик по элементу с локатором: {locator}")
    def click_to_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Не удалось кликнуть по элементу: {locator}"
        )
        element.click()
    
    
    @allure.step("Ввести текст в элемент {locator}")
    def send_keys_to_element(self, locator, text, time=10):
        element = self.find_element_with_wait(locator, time)
        element.clear()
        element.send_keys(text)
    
    
    @allure.step("Проскроллить страницу до элемента с локатором: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        _ = element.location_once_scrolled_into_view