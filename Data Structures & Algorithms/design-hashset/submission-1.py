class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> None:
        return key % self.size
        
    def add(self, key: int) -> None:
        location = self.hash(key)
        if key not in self.buckets[location]:
            self.buckets[location].append(key)

    def remove(self, key: int) -> None:
        location = self.hash(key)
        if key in self.buckets[location]:
            self.buckets[location].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self.hash(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)