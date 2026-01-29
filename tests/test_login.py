import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators import TestLocators
from helpers import login_user

class TestLogin:

    def test_login_from_main_page_button(self, driver, registered_user):
        """Проверка входа через кнопку 'Войти в аккаунт' на главной."""
        # 1. Открываем главную
        driver.get(Urls.MAIN_URL)
        
        # 2. Кликаем кнопку входа
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_MAIN))
        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()
        
        # 3. Вводим данные (через хелпер)
        login_user(driver, registered_user['email'], registered_user['password'])

        # 4. Проверка: успешный переход на главную
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.MAIN_URL))

    def test_login_from_personal_cabinet_button(self, driver, registered_user):
        """Проверка входа через кнопку 'Личный кабинет'."""
        driver.get(Urls.MAIN_URL)
        
        # 1. Кликаем Личный кабинет
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 2. Логинимся
        login_user(driver, registered_user['email'], registered_user['password'])

        # 3. Проверка
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.MAIN_URL))

    def test_login_from_registration_form(self, driver, registered_user):
        """Проверка входа через ссылку в форме регистрации."""
        driver.get(Urls.REGISTER_URL)
        
        # 1. Кликаем "Войти"
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_REGISTRATION))
        driver.find_element(*TestLocators.LOGIN_LINK_REGISTRATION).click()
        
        # 2. Логинимся
        login_user(driver, registered_user['email'], registered_user['password'])

        # 3. Проверка
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.MAIN_URL))

    def test_login_from_recovery_form(self, driver, registered_user):
        """Проверка входа через ссылку в форме восстановления пароля."""
        driver.get(Urls.FORGOT_PASSWORD_URL)
        
        # 1. Кликаем "Войти"
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_RECOVERY))
        driver.find_element(*TestLocators.LOGIN_LINK_RECOVERY).click()
        
        # 2. Логинимся
        login_user(driver, registered_user['email'], registered_user['password'])

        # 3. Проверка
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.MAIN_URL))
        