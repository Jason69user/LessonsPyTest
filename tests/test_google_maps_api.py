from utils.api import GoogleMapsApi
from requests import Response


class TestCreatePlace:

    # тест передачи данных через метод POST, PUT, DELETE и GET
    def test_create_new_place(self):
        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        json_post = result_post.json()
        place_id = json_post.get("place_id")
        assert result_post.status_code == 200
        print(f"Статус-код {result_post.status_code} POST корректный")

        print("Метод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        status_get = result_get.status_code
        assert status_get == 200
        print(f"Статус-код {status_get} GET корректный")

        print("Метод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)
        assert result_put.status_code == 200
        print(f"Статус-код {result_post.status_code} PUT корректный")

        print("Метод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        status_get = result_get.status_code
        assert status_get == 200
        print(f"Статус-код {status_get} GET корректный")

        print("Метод DELETE")
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)
        status_delete = result_delete.status_code
        assert status_delete == 200
        print(f"Статус-код {status_delete} DELETE корректный")

        print("Метод GET DELETE")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        status_get = result_get.status_code
        assert status_get == 404
        print(f"Статус-код {status_get} GET корректный")