import time
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators import OrderPageLocators


class OrderPage(BasePage):
    

    @allure.step("Заполнить форму 'Для кого самокат': Имя={name}, Фамилия={surname}, Телефон={phone}")
    def fill_first_order_form(self, name, surname, address, metro_station, phone):
        self.send_keys_to_element(OrderPageLocators.INPUT_NAME, name)
        self.send_keys_to_element(OrderPageLocators.INPUT_SURNAME, surname)
        self.send_keys_to_element(OrderPageLocators.INPUT_ADDRESS, address)
        self.select_metro_station(metro_station)
        self.send_keys_to_element(OrderPageLocators.INPUT_PHONE, phone)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    
    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        self.click_to_element(OrderPageLocators.INPUT_METRO_FIELD)
        formatted_xpath = OrderPageLocators.METRO_OPTION_TEMPLATE[1].format(station_name)

        ready_locator = (OrderPageLocators.METRO_OPTION_TEMPLATE[0], formatted_xpath)
        self.click_to_element(ready_locator)
    
    @allure.step("Заполнить форму 'Про аренду': Дата={date}, Срок={duration}, Цвет={color}, Комментарий={comment}")
    def fill_second_order_form(self, date, duration, color, comment):
        date_field = self.find_element_with_wait(OrderPageLocators.INPUT_DATE)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.select_rent_duration(duration)
        self.select_scooter_color(color)
        self.send_keys_to_element(OrderPageLocators.INPUT_COMMENT, comment)
        self.click_to_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)

    @allure.step("Выбрать срок аренды: {duration_text}")
    def select_rent_duration(self, duration_text):
        self.click_to_element(OrderPageLocators.DROPDOWN_RENT_DURATION)

        formatted_xpath = OrderPageLocators.RENT_DURATION_OPTION[1].format(duration_text)
        ready_locator = (OrderPageLocators.RENT_DURATION_OPTION[0], formatted_xpath)

        self.click_to_element(ready_locator)


    @allure.step("Выбрать цвет самоката: {color_name}")
    def select_scooter_color(self, color_name):
        if color_name == "black":
            self.click_to_element(OrderPageLocators.CHECKBOX_BLACK)
        elif color_name == "grey":
            self.click_to_element(OrderPageLocators.CHECKBOX_GREY)

    @allure.step("Подтвердить заказ в поп-апе кнопкой 'Да'")
    def confirm_order_in_popup(self):
        button_yes = self.wait_element_to_be_clickable(OrderPageLocators.BUTTON_YES)
        time.sleep(0.5)
        button_yes.click()
    @allure.step("Получить текст заголовка об успешном создании заказа")     
    def get_success_popup_header_text(self):
        element = self.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS_POPUP_HEADER)
        return element.text    
    




       
        