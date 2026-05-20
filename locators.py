from selenium.webdriver.common.by import By



class MainPageLocators:
    """Локаторы для Главной страницы (Яндекс.Самокат)"""
    # Локаторы для раздела FAQ (вопросы и ответы)
    FAQ_QUESTION_TEMPLATE = (By.XPATH, ".//div[@class='accordion__button' and text()='{}']")
    FAQ_ANSWER_TEMPLATE= (By.XPATH, ".//div[@class='accordion__panel']/p[text()='{}']")
    
    # Верхняя кнопка "Заказать" в шапке страницы
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") 
    
    
    # Нижняя кнопка "Заказать" на странице
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton__1_cWm')]/button[text()='Заказать']") 
    

    
    # Логотип «Самокат» (должен вести на главную Самоката)
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']/parent::a") 
    
    # Логотип «Яндекс» (должен вести на Дзен через редирект)
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']/parent::a") 


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""
    
  
    INPUT_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")      # Поле '* Имя'
    INPUT_SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")   # Поле '* Фамилия'
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")   # Поле '* Адрес: куда привезти заказ'
    
    # Поле '* Станция метро' 
    INPUT_METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']") 
    # Элемент станции метро в выпадающем списке (чтобы кликнуть по конкретному названию)
    
    METRO_OPTION_TEMPLATE = (By.XPATH, ".//div[contains(@class, 'select-search')]//button[div[text()='{}']]")
    
    INPUT_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")     # Поле '* Телефон: на него позвонит курьер'
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")     # Кнопка «Далее»

    
    INPUT_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")      # Поле '* Когда привезти самокат'
    
    DROPDOWN_RENT_DURATION = (By.XPATH, ".//div[@class='Dropdown-control']") # Поле '* Срок аренды' (выпадающий список)
    # Элемент срока аренды из списка 
    RENT_DURATION_OPTION = (By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='{}']") 
    
    # Чекбоксы выбора цвета самоката 
    COLOR_CHECKBOX_TEMPLATE = (By.ID, "{}")
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    
    INPUT_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")   # Поле 'Комментарий для курьера'
    
    # Кнопка «Заказать» под формой
    BUTTON_CONFIRM_ORDER = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Кнопка «Да» в поп-апе подтверждения заказа ("Хотите оформить заказ?")
    BUTTON_YES = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]//button[text()='Да']") 

  # Заголовок всплывающего окна об успешном заказе ("Заказ оформлен")
    ORDER_SUCCESS_POPUP_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
