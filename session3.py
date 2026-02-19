class Queue:
    def __init__(self, max_size=100):
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if self.rear >= len(self.list) - 1:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            return
        self.rear += 1
        self.list[self.rear] = x

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        k = self.list[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return k


# مثال استفاده
test = Queue(3)
test.insert(57)
test.insert(32)
test.insert(44)
test.insert(39)  # Queue is Full
test.delete()
test.insert(39)  # موفق


class C_Queue:
    def __init__(self, max_size):
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def insert(self, x):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            return
        self.rear = (self.rear + 1) % self.max_size
        self.list[self.rear] = x

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        k = self.list[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return k

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

