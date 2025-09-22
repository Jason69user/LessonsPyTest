import json
from requests import Response


class Checking:

    # проверяем статус-код запроса
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Провал. Статус-код = {str(response.status_code)}"
        print(f"Успешно. Статус-код = " + str(response.status_code))

    # проверка наличия полей в запросе
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    # проверка содержимых полей
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + ' верен')

    # проверка содержимых полей по отдельным словам
    @staticmethod
    def check_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f"Слово {search_word} отсутствует"
        print("Слово " + search_word + " присутствует")