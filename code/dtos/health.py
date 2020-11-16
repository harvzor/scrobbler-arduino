class Health:
    status = ''
    @staticmethod
    def from_json(json):
        health = Health()

        health.status = json['status']

        return health

    def __str__(self):
        # return f'Health({self.status})'
        return 'Health({status})'.format(status=self.status)
