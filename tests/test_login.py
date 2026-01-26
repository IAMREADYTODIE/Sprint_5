import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import MAIN_URL, PROFILE_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from locators import TestLocators

class TestLogin:

    def login_user(self, driver, email, password):
        """Метод авторизации пользователя."""
        # Ждем появления полей
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TestLocators.LOGIN_EMAIL_FIELD))
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(email)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(password)
        
        # Кликаем "Войти"
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        # Ждем, пока кнопка "Войти" исчезнет (гарантия перехода из формы)
        WebDriverWait(driver, 15).until(EC.invisibility_of_element_located(TestLocators.LOGIN_BUTTON))

    @pytest.mark.parametrize("login_type, locator", [
        ("main_page_button", TestLocators.LOGIN_BUTTON_MAIN),
        ("personal_cabinet_button", TestLocators.PERSONAL_CABINET_BUTTON),
    ])
    def test_login_from_main_page_elements(self, driver, registered_user, login_type, locator):
        """Вход через элементы на главной странице."""
        driver.get(MAIN_URL)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        
        self.login_user(driver, registered_user['email'], registered_user['password'])

        # Проверка: переходим в личный кабинет, чтобы подтвердить статус авторизации
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        # Если в профиле появилась кнопка Выход - тест прошел
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
        assert PROFILE_URL in driver.current_url

    @pytest.mark.parametrize("login_type, locator", [
        ("registration_link", TestLocators.LOGIN_LINK_REGISTRATION),
        ("recovery_link", TestLocators.LOGIN_LINK_RECOVERY),
    ])
    def test_login_from_form_links(self, driver, registered_user, login_type, locator):
        """Вход через ссылки в формах регистрации и восстановления."""
        if login_type == "registration_link":
            driver.get(REGISTER_URL)
        else:
            driver.get(FORGOT_PASSWORD_URL)
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        
        self.login_user(driver, registered_user['email'], registered_user['password'])

        # Проверка авторизации через переход в профиль
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
        
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
        assert PROFILE_URL in driver.current_url