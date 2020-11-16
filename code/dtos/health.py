class Health:
    status = ''
    @staticmethod
    def from_obj(obj):
        health = Health()

        health.status = obj['status']

        return health

    def __str__(self):
        # return f'Health({self.status})'
        return 'Health({status})'.format(status=self.status)
