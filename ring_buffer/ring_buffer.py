class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def append(self, item):
        self.item = item
        if (len(self.storage)) < self.capacity:
            self.storage.append(self.item)
            return self.storage
        elif (len(self.storage)) >= self.capacity:
            self.storage.pop(self.count)
            self.storage.insert(self.count, item)
            if self.count+1 >= self.capacity:
                self.count = 0
            else:
                self.count +=1
            return self.storage

    def get(self):
        return self.storage

# ring = RingBuffer(3)
# ring.append(1)
# print(ring.storage)
# ring.append(2)
# print(ring.storage)
# ring.append(3)
# print(ring.storage)
# ring.append(4)
# print(ring.storage)
# ring.append(5)
# print(ring.storage)
# ring.append(6)
# print(ring.storage)
# ring.append(7)
# print(ring.storage)
# ring.append(8)
# print(ring.storage)
