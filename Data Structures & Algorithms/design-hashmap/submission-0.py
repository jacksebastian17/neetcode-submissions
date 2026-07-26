class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self.hash(key)]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self.hash(key)]
        return next((v for k, v in bucket if k == key), -1)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self.hash(key)]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
key,value = (1,1)     -> hash(1)    = 1 % 1000    = 1 -> buckets[1] = [(1, 1)]
key,value = (1001,42) -> hash(1001) = 1001 % 1000 = 1 -> buckets[1] = [(1,1),(1001, 42)]
"""