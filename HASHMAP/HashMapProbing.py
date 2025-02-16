class HashMapProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:  # Table full
                raise Exception("HashMap is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None  # Key not found

    def display(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")

# Example Usage:
hmap = HashMapProbing(5)
hmap.insert(1, "A")
hmap.insert(6, "B")  # Collides with 1, goes to next available slot
hmap.display()
print("Search 6:", hmap.search(6))
