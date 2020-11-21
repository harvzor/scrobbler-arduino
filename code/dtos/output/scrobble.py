class Scrobble:
    id = 0
    item_id = ''
    timestamp = ''

    @staticmethod
    def from_obj(obj):
        scrobble = Scrobble()

        scrobble.id = obj['id']
        scrobble.item_id = obj['drink_id']
        scrobble.timestamp = obj['drank_timestamp']

        return scrobble

    @staticmethod
    def from_objs(objs):
        scrobbles = []

        for obj in objs:
            scrobbles.append(Scrobble.from_obj(obj))
        
        return scrobbles
