import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import MAIN_URL, PROFILE_URL, LOGIN_URL
from locators import TestLocators

class TestPersonalCabinet:

    def test_go_to_personal_cabinet_authorized_user(self, driver, registered_user):
        """Проверка перехода в личный кабинет авторизованным пользователем."""
        # 1. Авторизация
        driver.get(LOGIN_URL)
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        # 2. Переход в Личный кабинет
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 3. Проверка: попали в профиль
        WebDriverWait(driver, 15).until(EC.url_to_be(PROFILE_URL))
        assert driver.current_url == PROFILE_URL

    def test_go_to_personal_cabinet_unauthorized_user_redirects_to_login(self, driver):
        """Проверка: неавторизованного пользователя при клике на 'Личный кабинет' редиректит на логин."""
        # 1. Заходим на главную неавторизованными
        driver.get(MAIN_URL)
        
        # 2. Кликаем Личный кабинет
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # 3. Проверка: нас перекинуло на страницу входа
        WebDriverWait(driver, 15).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    @pytest.mark.parametrize("locator", [
        TestLocators.CONSTRUCTOR_BUTTON,
        TestLocators.LOGO_BUTTON
    ])
    def test_go_from_cabinet_to_constructor(self, driver, registered_user, locator):
        """Проверка перехода из личного кабинета в конструктор через кнопку и логотип."""
        driver.get(LOGIN_URL)
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        
        WebDriverWait(driver, 15).until(EC.url_to_be(MAIN_URL))
        assert driver.current_url == MAIN_URL

    def test_logout(self, driver, registered_user):
        """Проверка выхода из аккаунта."""
        driver.get(LOGIN_URL)
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        
        WebDriverWait(driver, 15).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL