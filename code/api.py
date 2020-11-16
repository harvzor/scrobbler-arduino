import urequests
from dtos.health import Health
from dtos.drink import Drink
import env

def get(endpoint):
    print('GET ' + endpoint)

    res = urequests.get(endpoint)

    print('---')
    print('Status: ' + str(res.status_code))

    if res.status_code != 200:
        raise Exception('API returned non-200 code')

    return res.json()

def get_health():
    endpoint = env.api + '/health'

    obj = get(endpoint)

    return Health.from_obj(obj)

def get_drinks():
    endpoint = env.api + '/drinks'

    objs = get(endpoint)

    return Drink.from_objs(objs)
