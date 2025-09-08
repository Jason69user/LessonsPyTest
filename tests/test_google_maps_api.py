from utils.api import GoogleMapsApi
from requests import Response


class TestCreatePlace:

    # тест передачи данных через метод POST и GET
    def test_create_new_place(self):
        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        json_post = result_post.json()
        place_id = json_post.get("place_id")
        assert result_post.status_code == 200
        print(f"Статус-код {result_post.status_code} POST корректный\n")

        print("Метод GET")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        status_get = result_get.status_code
        assert status_get == 200
        print(f"Статус-код {status_get} GET корректный")