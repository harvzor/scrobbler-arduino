import urequests
from dtos.health import Health
from dtos.drink import Drink
import env

def get(endpoint):
    print('GET ' + endpoint)
    print('---')

    try:
        res = urequests.get(endpoint)

        print('Status: ' + str(res.status_code))

        if res.status_code != 200:
            return None

        return res.json()
    except:
        print('No response...')
        return None


def get_health():
    endpoint = env.api + '/health'

    obj = get(endpoint)

    if obj is None:
        return Health()

    return Health.from_obj(obj)

def get_drinks():
    endpoint = env.api + '/drinks'

    objs = get(endpoint)

    if objs is None:
        return None

    return Drink.from_objs(objs)
