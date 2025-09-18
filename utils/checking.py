import json

from requests import Response


class Checking:

    # проверяем статус-код запроса
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, print("Провал. Статус-код = " + str(response.status_code))
        print(f"Успешно. Статус-код = " + str(response.status_code))

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")