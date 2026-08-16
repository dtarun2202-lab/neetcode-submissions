class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]  # list of lists of (key,value) pairs

    def hash(self, key):
        return key % self.size                          # map key → bucket index

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):    # search for existing key
            if k == key:
                bucket[i] = (key, value)        # key exists → UPDATE value
                return

        bucket.append((key, value))             # key not found → INSERT new pair

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:                     # search bucket for key
            if k == key:
                return v                        # found → return value

        return -1                               # not found → return -1

    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):    # search for key
            if k == key:
                bucket.pop(i)                   # found → remove pair
                return