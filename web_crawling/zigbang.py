import requests
import geohash2
import pandas as pd

def oneroom(address):
    url = f'https://apis.zigbang.com/v2/search?leaseYn=N&q={address}&serviceType=원룸'
    response = requests.get(url)
    data = response.json()['items'][0]
    lat, lng = data['lat'], data['lng']

    geohash = geohash2.encode(lat, lng, precision=5)
    url = 'https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&'\
          f'&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸'

    response = requests.get(url)
    items = response.json()['items']

    ids = [item['item_id'] for item in items]

    get_item_list = 'https://apis.zigbang.com/v2/items/list'
    params = {"domain": "zigbang",
              "withCoalition": 'true',
              "item_ids": ids[:900]
              }

    response = requests.post(get_item_list, data=params)

    items = response.json()['items']
    df = pd.DataFrame(items)

    return df[['item_id', 'sales_type']]

print(oneroom('강남구 역삼동'))