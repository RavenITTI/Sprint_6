import pytest
from selenium import webdriver
from data import URLS

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(16)
    
    browser.get(URLS.BASE_URL)
    
    yield browser 
    
    browser.quit()