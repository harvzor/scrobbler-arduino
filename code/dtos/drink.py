class Drink:
    id = 0
    name = ''
    count = 0
    colour = ''
    deleted = False

    @staticmethod
    def from_obj(obj):
        drink = Drink()

        drink.id = obj['id']
        drink.name = obj['name']
        drink.count = obj['count']
        drink.colour = obj['colour']
        drink.deleted = obj['deleted']

        return drink

    @staticmethod
    def from_objs(objs):
        drinks = []

        for obj in objs:
            drinks.append(Drink.from_obj(obj))
        
        return drinks
