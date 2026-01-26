import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import REGISTER_URL, VALID_PASSWORD, INVALID_PASSWORD, LOGIN_URL
from locators import TestLocators
from helpers import generate_random_user


# Используем фикстуру driver из conftest.py
class TestRegistration:

    def test_successful_registration(self, driver):
        """Проверка: Успешная регистрация пользователя."""
        
        # 1. Подготовка данных
        user_data = generate_random_user()

        # 2. Действия
        driver.get(REGISTER_URL) # Открываем страницу регистрации
        
        # Ввод имени
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
        
        # Ввод email
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
        
        # Ввод валидного пароля
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
        
        # Нажатие на кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        
        # 3. Проверки (Assertion)
        # Ожидаем, что после регистрации нас перебросит на страницу входа
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        
        # Проверяем, что текущий URL соответствует странице входа
        assert driver.current_url == LOGIN_URL, f"Ожидался URL {LOGIN_URL}, получен {driver.current_url}"


    def test_registration_with_short_password_shows_error(self, driver):
        """Проверка: Ошибка при регистрации с паролем менее 6 символов."""
        
        # 1. Подготовка данных
        user_data = generate_random_user()
        
        # 2. Действия
        driver.get(REGISTER_URL)
        
        # Ввод валидных имени и email
        driver.find_element(*TestLocators.REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
        
        # Ввод невалидного пароля (3 символа)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD).send_keys(INVALID_PASSWORD)
        
        # Клик по кнопке регистрации
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        
        # 3. Проверки (Assertion)
        # Ожидаем, что появится сообщение об ошибке (оно должно быть видимым)
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PASSWORD_ERROR)
        )
        
        # Проверяем, что элемент ошибки содержит нужный текст (для двойной надежности)
        assert error_element.text == "Некорректный пароль", "Сообщение об ошибке не соответствует ожидаемому."
        
        # Проверяем, что нас не перебросило на страницу входа
        assert driver.current_url == REGISTER_URL, "Произошел несанкционированный переход со страницы регистрации."