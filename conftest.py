import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Urls, TestData
from locators import TestLocators
from helpers import generate_random_user

@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы браузера."""
    driver_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    driver.get(Urls.MAIN_URL)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def registered_user(driver):
    """Фикстура: регистрирует пользователя через UI и возвращает данные."""
    user_data = generate_random_user()
    
    driver.get(Urls.REGISTER_URL)
    
    # Ожидание готовности полей
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(TestLocators.REGISTRATION_NAME_FIELD)
    )
    
    # Заполнение формы
    driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
    driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
    driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(user_data['password'])
    
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    
    # Проверка перехода на страницу логина
    WebDriverWait(driver, 15).until(EC.url_to_be(Urls.LOGIN_URL))
    
    yield user_data
    
    