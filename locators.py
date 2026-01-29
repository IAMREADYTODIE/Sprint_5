from selenium.webdriver.common.by import By

class TestLocators:
    # --- РЕГИСТРАЦИЯ ---
    REGISTRATION_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input")
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]")

    # --- ВХОД (Кнопки-переходы) ---
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']")
    LOGIN_LINK_REGISTRATION = (By.XPATH, ".//a[text()='Войти']")
    LOGIN_LINK_RECOVERY = (By.XPATH, ".//a[text()='Войти']")

    # --- ФОРМА ВХОДА (Поля и кнопка) ---
    LOGIN_EMAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # --- ЛИЧНЫЙ КАБИНЕТ ---
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']")
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class, 'logo')]/a")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # --- КОНСТРУКТОР (Разделы) ---
    TAB_BUNS = (By.XPATH, ".//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    TAB_FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    