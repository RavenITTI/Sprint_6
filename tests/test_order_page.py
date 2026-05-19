import allure
import pytest
from pages.main_page import MainPage  
from pages.order_page import OrderPage
@allure.epic("Сервис Яндекс.Самокат")
@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий заказа через разные точки входа")
class TestOrder:
 @allure.title("Создание заказа. Точка входа: {button_type}, Пользователь: {name}")
 @pytest.mark.parametrize(
    "button_type, name, surname, address, metro_station, phone, date, duration, color, comment",
    [
        # Набор №1
        ("top", "Чумба", "Кибергон", "ул. Ленина, д. 10, кв. 5", "Сокольники", "89991112233", "25.05.2026", "сутки", "black", "Позвоните за полчаса"),
        # Набор №2
        ("bottom", "Василий", "Пупкин", "г. Москва, ул. Мира, д. 1", "Черкизовская", "89112223344", "26.05.2026", "двое суток", "grey", "Оставьте у двери")
    ]
)
 def test_scooter_order_positive(self, driver, button_type, name, surname, address, metro_station, phone, date, duration, color, comment):
     main_page = MainPage(driver)
     main_page.open_site()
    
   
     if button_type == "top":
        main_page.click_top_order_button()
     else:
        main_page.click_bottom_order_button()
        
     order_page = OrderPage(driver)
    
  
     order_page.fill_first_order_form(
         name=name,
         surname=surname,
         address=address,
         metro_station=metro_station,
         phone=phone
    )
    
  
     order_page.fill_second_order_form(
         date=date,
         duration=duration,
         color=color,
         comment=comment
    )
    
   
     order_page.confirm_order_in_popup()
    
   
     success_text = order_page.get_success_popup_header_text()
     assert "Заказ оформлен" in success_text