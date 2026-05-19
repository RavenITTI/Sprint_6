import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators import MainPageLocators, URLS



@allure.epic("Сервис Яндекс.Самокат")
@allure.feature("Навигация и переходы (Логотипы)")
class TestLogos:
 @allure.story("Клик на логотип 'Самокат'")
 @allure.title("Проверка возврата на главную страницу при клике на логотип 'Самокат'")
 def test_click_scooter_logo_opens_main_page(self, driver):
     main_page = MainPage(driver)
     main_page.open_site()
     main_page.click_top_order_button()
    
     order_page = OrderPage(driver)
     order_page.click_to_element(MainPageLocators.SCOOTER_LOGO)

     assert driver.current_url == URLS.BASE_URL

 @allure.story("Клик на логотип 'Яндекс'")
 @allure.title("Проверка перехода на Дзен при клике на логотип 'Яндекс'")
 def test_click_yandex_logo_redirects_to_dzen(self, driver):
     main_page = MainPage(driver)
     main_page.open_site()
    
     original_window = driver.current_window_handle

     main_page.click_to_element(MainPageLocators.YANDEX_LOGO)

     for window_handle in driver.window_handles:
         if window_handle != original_window:
             driver.switch_to.window(window_handle)
             break
            
     time.sleep(3)

     assert "dzen.ru" in driver.current_url