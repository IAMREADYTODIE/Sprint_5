import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators import TestLocators
from helpers import login_user

class TestPersonalCabinet:

    def test_go_to_personal_cabinet_authorized_user(self, driver, registered_user):
        """Проверка перехода в ЛК авторизованным пользователем."""
        # 1. Авторизация
        login_user(driver, registered_user['email'], registered_user['password'])
        
        # 2. Переход в Личный кабинет
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 3. Проверка: попали в профиль
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.PROFILE_URL))

    def test_go_to_personal_cabinet_unauthorized_user(self, driver):
        """Проверка перехода в ЛК неавторизованным пользователем."""
        driver.get(Urls.MAIN_URL)
        
        # 1. Кликаем Личный кабинет
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 2. Проверка: редирект на логин
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.LOGIN_URL))

    @pytest.mark.parametrize("locator", [
        TestLocators.CONSTRUCTOR_BUTTON,
        TestLocators.LOGO_BUTTON
    ])
    def test_go_from_cabinet_to_constructor(self, driver, registered_user, locator):
        """Проверка перехода из ЛК в конструктор."""
        # 1. Логин и вход в ЛК
        login_user(driver, registered_user['email'], registered_user['password'])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 2. Клик на элемент перехода
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        
        # 3. Проверка: мы на главной
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.MAIN_URL))

    def test_logout(self, driver, registered_user):
        """Проверка выхода из аккаунта."""
        # 1. Логин и вход в ЛК
        login_user(driver, registered_user['email'], registered_user['password'])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 2. Выход
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        
        # 3. Проверка: мы на странице логина
        assert WebDriverWait(driver, 15).until(EC.url_to_be(Urls.LOGIN_URL))
        