import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls, TestData
from locators import TestLocators
from helpers import generate_random_user

class TestRegistration:

    def test_successful_registration(self, driver):
        """Проверка: Успешная регистрация пользователя."""
        # 1. Подготовка данных
        user_data = generate_random_user()

        # 2. Действия
        driver.get(Urls.REGISTER_URL)
        
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        
        # 3. Проверка: ожидаем переход на страницу входа (сразу в assert)
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.LOGIN_URL))

    def test_registration_with_short_password_shows_error(self, driver):
        """Проверка: Ошибка при регистрации с некорректным паролем."""
        # 1. Подготовка данных
        user_data = generate_random_user()
        
        # 2. Действия
        driver.get(Urls.REGISTER_URL)
        
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(TestData.INVALID_PASSWORD)
        
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        
        # 3. Проверка: ожидаем появление ошибки и проверяем текст
        error_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(TestLocators.PASSWORD_ERROR)
        )
        assert error_element.text == "Некорректный пароль"
        