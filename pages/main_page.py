import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    
    @allure.step("Кликнуть по верхней кнопке 'Заказать' в шапке")
    def click_top_order_button(self):
        self.click_to_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть по нижней кнопке 'Заказать' внизу страницы")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
   
   
    @allure.step("Кликнуть по вопросу в FAQ под номером {index}")
    def click_faq_question(self, index):
        
        formatted_xpath = MainPageLocators.FAQ_QUESTION_TEMPLATE[1].format(index)
        ready_locator = (MainPageLocators.FAQ_QUESTION_TEMPLATE[0], formatted_xpath)
        
        self.scroll_to_element(ready_locator)
        self.click_to_element(ready_locator)


    @allure.step("Получить текст ответа в FAQ под номером {index}")
    def get_faq_answer_text(self, index):
       
        formatted_xpath = MainPageLocators.FAQ_ANSWER_TEMPLATE[1].format(index)
        ready_locator = (MainPageLocators.FAQ_ANSWER_TEMPLATE[0], formatted_xpath)
        
        element = self.find_element_with_wait(ready_locator)
        return element.text