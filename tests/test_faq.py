import allure
import pytest
from pages.main_page import MainPage
from data import FAQData

@allure.epic("Сервис Яндекс.Самокат")
@allure.feature("Главная страница")
@allure.story("Блок 'Вопросы о важном' (FAQ)")
class TestFaq:
  @allure.title("Проверка раскрытия вопроса и соответствия текста ответа")
  @pytest.mark.parametrize('question, answer', FAQData.FAQ_DATA)
  def test_faq(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.open_site()
        
        
        assert main_page.click_and_check_faq(question, answer)