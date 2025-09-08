from utils.httpmethods import HttpMethods


base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        # тело запроса POST
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # путь запроса POST
        post_resourse = "/maps/api/place/add/json"
        post_url = base_url + post_resourse + key
        print(post_url)
        # старт метода POST
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

# Проверяем полученный place_id через GET метод
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id" + place_id
        print(get_url)
        # старт метода GET
        resul_get = HttpMethods.get(get_url)
        print(resul_get.text)
        return resul_get