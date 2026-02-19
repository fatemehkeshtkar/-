class C_Queue:
    def __init__(self, max_size=100):
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
            self.list[0] = x
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

    def show_valid(self):
        if self.is_empty():
            print("Queue is empty")
            return
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.list[i])
        else:
            for i in range(self.front, self.max_size):
                print(self.list[i])
            for i in range(0, self.rear + 1):
                print(self.list[i])

    def show_invalid(self):
        if self.is_empty():
            for i in range(self.max_size):
                print(self.list[i])
            return
        i = (self.rear + 1) % self.max_size
        while i != self.front:
            print(self.list[i])
            i = (i + 1) % self.max_size

    def find(self, x):
        if self.is_empty():
            return -1
        i = self.front
        if self.list[i] == x:
            return i
        while i != self.rear:
            i = (i + 1) % self.max_size
            if self.list[i] == x:
                return i
        return -1

    def replace(self, x, y):
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            self.list[i] = y
        while i != self.rear:
            i = (i + 1) % self.max_size
            if self.list[i] == x:
                self.list[i] = y
