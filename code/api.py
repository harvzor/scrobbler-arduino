import urequests
from dtos.health import Health
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

    json = get(endpoint)

    return Health.from_json(json)
