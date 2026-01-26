import random
import string

def generate_random_user():
    """Генерирует уникальный логин, имя и пароль для регистрации. 
    Используется для обеспечения атомарности тестов."""
    
    # Генерация уникальной части почты
    test_prefix = ''.join(random.choices(string.ascii_lowercase, k=8))
    test_email = f'{test_prefix}_{random.randint(100, 999)}@yandex.ru'

    # Генерация пароля (минимум 6 символов)
    test_password = 'Pass' + str(random.randint(1000, 9999))
    
    return {
        'name': f'User_{random.randint(100, 999)}',
        'email': test_email,
        'password': test_password
    }