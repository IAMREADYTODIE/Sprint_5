import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import MAIN_URL, REGISTER_URL, LOGIN_URL
from locators import TestLocators
from helpers import generate_random_user

@pytest.fixture
def driver():
    """Инициализация и завершение работы драйвера Chrome."""
    driver_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    driver.get(MAIN_URL)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def registered_user(driver):
    """Регистрация нового пользователя через UI и возврат его учетных данных."""
    user_data = generate_random_user()
    
    driver.get(REGISTER_URL)
    
    # Ожидание готовности полей ввода
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(TestLocators.REGISTRATION_NAME_FIELD)
    )
    
    # Заполнение формы регистрации
    driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
    driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
    driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(user_data['password'])
    
    # Клик по кнопке регистрации
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    
    # Ожидание перехода на страницу логина как подтверждение успешной регистрации
    WebDriverWait(driver, 15).until(EC.url_to_be(LOGIN_URL))

    return user_data
    