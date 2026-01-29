import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def generate_random_user():
    """Генерирует уникальный логин, имя и пароль для регистрации."""
    test_prefix = ''.join(random.choices(string.ascii_lowercase, k=8))
    test_email = f'{test_prefix}_{random.randint(100, 999)}@yandex.ru'
    test_password = 'Pass' + str(random.randint(1000, 9999))
    
    return {
        'name': f'User_{random.randint(100, 999)}',
        'email': test_email,
        'password': test_password
    }

def login_user(driver, email, password):
    """Вспомогательный метод: вводит данные и нажимает кнопку входа."""
    # Ждем, пока поля станут доступны
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGIN_EMAIL_FIELD))
    
    # Вводим данные
    driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(password)
    
    # Кликаем "Войти"
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    
    # Ждем исчезновения кнопки "Войти" (знак, что логин прошел)
    WebDriverWait(driver, 15).until(EC.invisibility_of_element_located(TestLocators.LOGIN_BUTTON))
    