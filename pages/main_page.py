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
   
   
    @allure.step('Клик по вопросу и проверка ответа')
    def click_and_check_faq(self, question, answer):
       
        q_loc = (MainPageLocators.FAQ_QUESTION_TEMPLATE[0], MainPageLocators.FAQ_QUESTION_TEMPLATE[1].format(question))
        a_loc = (MainPageLocators.FAQ_ANSWER_TEMPLATE[0], MainPageLocators.FAQ_ANSWER_TEMPLATE[1].format(answer))
      
        self.scroll_to_element(q_loc)
        self.click_to_element(q_loc)
        
        
        return self.find_element_with_wait(a_loc).is_displayed()