import urequests
import ujson

from dtos.output.health import Health
from dtos.output.trackable import Trackable
from dtos.output.scrobble import Scrobble
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

def post(endpoint, data):
    json_data = ujson.dumps(data.__dict__)

    print('POST ' + endpoint)
    print(json_data)
    print('---')

    try:
        res = urequests.post(endpoint, headers = {'content-type': 'application/json'}, data = json_data)

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

def get_trackables():
    endpoint = env.api + '/trackables'

    objs = get(endpoint)

    if objs is None:
        return None

    return Trackable.from_objs(objs)

def post_scrobble(trackable_id):
    from dtos.input.scrobble_post import ScrobblePost
    
    scrobble_post = ScrobblePost()

    scrobble_post.trackable_id = trackable_id

    endpoint = env.api + '/scrobbles'

    obj = post(endpoint, scrobble_post)

    if obj is None:
        return None
    
    return Scrobble.from_obj(obj)
