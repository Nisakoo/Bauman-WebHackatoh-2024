import json
import requests


# r = requests.post("http://127.0.0.1:8000/model/ranking", json={
#     "x": [[5, 2, -1, 0],
#           [1, 10, 0, 10]],
#     "weights": [0, 2, 0, 4, 0],
# })

# r = requests.post("http://127.0.0.1:8000/model/learning", json={
#     "x": [[5, 2, -1, 0]],
#     "y": [2],
#     "weights": [0, 2, 0, 4, 0],
# })

# r = requests.post("http://127.0.0.1:8000/events/get", json={
#     "calendar_url": "https://calendar.google.com/calendar/ical/2f32dd8c6d8dee2b007fc9627557fd9ca555a66ec908e0a0bc57244bfebc1f7e%40group.calendar.google.com/public/basic.ics"
# })

# print(r.text)


def get_user_location():
    response = requests.get('')
    data = response.json()
    return data['lat'], data['lon']

def find_nearest_restaurants(lat, lon, api_key):
    url = f'https://catalog.api.2gis.com/3.0/items'
    params = {
        'q': 'ресторан',
        'point': f'{lon},{lat}',
        'radius': 3000,  # Радиус поиска в метрах
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()


def main():
    api_key = 'b958d355-454a-4241-8a6d-2b86acdae86f'
    lat, lon = get_user_location()
    print(f'Ваше местоположение: широта {lat}, долгота {lon}')

    restaurants = find_nearest_restaurants(lat, lon, api_key)
    print(restaurants)
    # for restaurant in restaurants.get('result', {}).get('items', []):
    #     name = restaurant.get('name')
    #     address = restaurant.get('address_name')
    #     ranking = restaurant.get('ranking')
    #     print(f'Ресторан: {name}, Адрес: {address}')

def get_geocode(**kwargs):
    base_url = "https://catalog.api.2gis.com/3.0/item/4504235282645692"
    api_key = "b958d355-454a-4241-8a6d-2b86acdae86f"

    kwargs.update(dict(key=api_key))
    resp = requests.get(base_url, params=kwargs)

    return json.loads(resp.text)


if __name__ == "__main__":
    print(get_geocode(fields="fields=item.rating"))
    print(get_geocode(q="Москва, 2-я Бауманская 5с1", fields="fields=items.point,items.geometry.centroid"))
    # main()
