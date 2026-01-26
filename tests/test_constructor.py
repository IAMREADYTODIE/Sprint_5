import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestConstructor:

    def test_go_to_sauces_section(self, driver):
        """Проверка перехода к разделу 'Соусы'."""
        # 1. Кликаем на вкладку "Соусы"
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        
        # 2. Проверяем, что у элемента вкладки появился класс текущего раздела
        # Мы ждем, пока в атрибуте class появится подстрока 'tab_type_current'
        WebDriverWait(driver, 10).until(
            lambda d: "tab_type_current" in d.find_element(*TestLocators.TAB_SAUCES).get_attribute("class")
        )
        
        current_class = driver.find_element(*TestLocators.TAB_SAUCES).get_attribute("class")
        assert "tab_type_current" in current_class

    def test_go_to_fillings_section(self, driver):
        """Проверка перехода к разделу 'Начинки'."""
        # 1. Кликаем на вкладку "Начинки"
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        
        # 2. Проверяем наличие класса 'tab_type_current'
        WebDriverWait(driver, 10).until(
            lambda d: "tab_type_current" in d.find_element(*TestLocators.TAB_FILLINGS).get_attribute("class")
        )
        
        current_class = driver.find_element(*TestLocators.TAB_FILLINGS).get_attribute("class")
        assert "tab_type_current" in current_class

    def test_go_to_buns_section(self, driver):
        """Проверка перехода к разделу 'Булки'."""
        # Чтобы проверить переход на Булки, нужно сначала уйти на другой раздел, 
        # так как Булки выбраны по умолчанию.
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        
        # 1. Теперь возвращаемся на "Булки"
        driver.find_element(*TestLocators.TAB_BUNS).click()
        
        # 2. Проверяем наличие класса 'tab_type_current'
        WebDriverWait(driver, 10).until(
            lambda d: "tab_type_current" in d.find_element(*TestLocators.TAB_BUNS).get_attribute("class")
        )
        
        current_class = driver.find_element(*TestLocators.TAB_BUNS).get_attribute("class")
        assert "tab_type_current" in current_class