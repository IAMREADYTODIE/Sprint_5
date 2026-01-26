# Базовый URL
MAIN_URL = 'https://stellarburgers.education-services.ru/'

# URLы для форм 
LOGIN_URL = f'{MAIN_URL}login'
REGISTER_URL = f'{MAIN_URL}register'
FORGOT_PASSWORD_URL = f'{MAIN_URL}forgot-password'
PROFILE_URL = f'{MAIN_URL}account/profile'

# Пароли
VALID_PASSWORD = '123456'  # Минимально 6 символов для успешной регистрации
INVALID_PASSWORD = '123'  # Менее 6 символов для проверки ошибки