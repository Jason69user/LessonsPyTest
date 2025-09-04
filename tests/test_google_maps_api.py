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
        print("Статус-код POST корректный")