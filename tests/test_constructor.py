import pytest
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators

class TestConstructor:

    def test_go_to_sauces_section(self, driver):
        """Проверка перехода к разделу 'Соусы'."""
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        
        # Проверяем, что класс содержит активное состояние (прямо в ожидании)
        assert WebDriverWait(driver, 10).until(
            lambda d: "tab_type_current" in d.find_element(*TestLocators.TAB_SAUCES).get_attribute("class")
        )

    def test_go_to_fillings_section(self, driver):
        """Проверка перехода к разделу 'Начинки'."""
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        
        assert WebDriverWait(driver, 10).until(
            lambda d: "tab_type_current" in d.find_element(*TestLocators.TAB_FILLINGS).get_attribute("class")
        )

    def test_go_to_buns_section(self, driver):
        """Проверка перехода к разделу 'Булки'."""
        # Уходим на другой раздел, чтобы потом вернуться
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        
        driver.find_element(*TestLocators.TAB_BUNS).click()
        
        assert WebDriverWait(driver, 10).until(
            lambda d: "tab_type_current" in d.find_element(*TestLocators.TAB_BUNS).get_attribute("class")
        )
        