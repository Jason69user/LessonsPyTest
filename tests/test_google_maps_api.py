from utils.api import GoogleMapsApi
from requests import Response

class TestCreatePlace:

    # тест передачи данных через метод POST
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()