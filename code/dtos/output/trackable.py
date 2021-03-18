class Trackable:
    id = 0
    name = ''
    count = 0
    colour = ''
    deleted = False

    @staticmethod
    def from_obj(obj):
        trackable = Trackable()

        trackable.id = obj['id']
        trackable.name = obj['name']
        trackable.count = obj['count']
        trackable.colour = obj['colour']
        trackable.deleted = obj['deleted']

        return trackable

    @staticmethod
    def from_objs(objs):
        trackables = []

        for obj in objs:
            trackables.append(Trackable.from_obj(obj))
        
        return trackables
