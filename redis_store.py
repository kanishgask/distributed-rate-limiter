class RedisStore:

    def __init__(self):
        self.store = {}

    def increment(self, key):

        if key not in self.store:
            self.store[key] = 0

        self.store[key] += 1

        return self.store[key]

    def get(self, key):

        return self.store.get(key)
