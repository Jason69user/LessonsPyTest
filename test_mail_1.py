import pytest


# авторизация в системе
@pytest.fixture
def set_up():
    print("Вход в систему выполнен")

# отправляем первое письмо
def test_sending_mail_1(set_up):
    print("Письмо отправлено")

# отправляем второе письмо
def test_sending_mail_2(set_up):
    print("Письмо отправлено")