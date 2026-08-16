class MyHashSet:

    def __init__(self):
        self.size = 1000                        # number of buckets
        self.buckets = [[] for _ in range(self.size)]  # each bucket is a list

    def hash(self, key):
        return key % self.size                  # hash function → index

    def add(self, key):
        index = self.hash(key)
        if key not in self.buckets[index]:      # avoid duplicates
            self.buckets[index].append(key)

    def remove(self, key):
        index = self.hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key):
        index = self.hash(key)
        return key in self.buckets[index]       # True or False