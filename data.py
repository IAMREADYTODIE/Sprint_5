class Urls:
    # Базовый URL
    MAIN_URL = 'https://stellarburgers.education-services.ru/'
    
    # URLы страниц
    LOGIN_URL = f'{MAIN_URL}login'
    REGISTER_URL = f'{MAIN_URL}register'
    FORGOT_PASSWORD_URL = f'{MAIN_URL}forgot-password'
    PROFILE_URL = f'{MAIN_URL}account/profile'

class TestData:
    # Пароли
    VALID_PASSWORD = '123456'  # Минимально 6 символов
    INVALID_PASSWORD = '123'   # Невалидный пароль
    