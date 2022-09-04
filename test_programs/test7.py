class HashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        total_sum = 0
        for letter in key:
            total_sum += ord(letter)
        return total_sum % self.MAX

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        while self.arr[hash]:
            if not self.arr[hash]:
                break
            hash += 1
            if hash >= len(self.arr):
                hash = 0
        self.arr[hash] = (key, value)

    def __getitem__(self, key):
        hash = self.get_hash(key)
        if self.arr[hash] == None:
            return
        for i in self.get_prob_range(hash):
            if self.arr[i][0] == key:
                return self.arr[i][1]

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]

    def __delitem__(self, key):
        hash = self.get_hash(key)
        if self.arr[hash] == None:
            return
        for i in self.get_prob_range(hash):
            if self.arr[i][0] == key:
                self.arr[i] = None
                return


ht = HashTable()
print(ht.get_hash("march 6"))
print(ht.get_hash("march 17"))
ht["march 6"] = 15
ht["march 17"] = 20
ht["march 4"] = 12
# del ht["march 6"]
print(ht.get_prob_range(9))
print(ht["march 6"])
