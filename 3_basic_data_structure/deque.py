class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()