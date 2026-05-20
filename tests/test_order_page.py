import allure
import pytest
from pages.main_page import MainPage  
from pages.order_page import OrderPage
from data import OrderData

@allure.epic("Сервис Яндекс.Самокат")
@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий заказа через разные точки входа")
class TestOrder:
 @allure.title("Создание заказа. Точка входа: {button_type}, Пользователь: {name}")
 @pytest.mark.parametrize(
        "button_method, client_name, user_data",
        [
            ("click_top_order_button", "Чумба", OrderData.CHUMBA_DATA),
            ("click_bottom_order_button", "Василий", OrderData.VASILY_DATA)
        ]
    )
 def test_scooter_order_positive(self, driver, button_method, client_name, user_data):
        main_page = MainPage(driver)
        main_page.open_site()
        
       
        getattr(main_page, button_method)()
         
        order_page = OrderPage(driver)
     
        
        order_page.fill_first_order_form(
            name=user_data["name"],
            surname=user_data["surname"],
            address=user_data["address"],
            metro_station=user_data["metro_station"],
            phone=user_data["phone"]
        )
     
        # Заполняем вторую форму
        order_page.fill_second_order_form(
            date=user_data["date"],
            duration=user_data["duration"],
            color=user_data["color"],
            comment=user_data["comment"]
        )
     
        order_page.confirm_order_in_popup()
     
        success_text = order_page.get_success_popup_header_text()
        assert "Заказ оформлен" in success_text