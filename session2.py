class Stack:
    def __init__(self, limit=1000):
        self.st = []
        self.lim = limit

    def push(self, x):
        if len(self.st) >= self.lim:
            print("stack is full")
            return -1
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            print("stack is empty")
            return -1
        return self.st.pop()

    def peek(self):
        if len(self.st) == 0:
            print("stack is empty")
            return -1
        return self.st[-1]

    # ایندکس(x) های درون پشته را برگرداند
    def find(self, x):
        indices = []
        for i in range(len(self.st)):
            if self.st[i] == x:
                indices.append(i)
        return indices

    # اولین شامل (x) را برگرداند
    def find1(self, x):
        for i in range(len(self.st)):
            if self.st[i] == x:
                return i
        return -1

    # آخرین ایندکس شامل (x) را برگرداند
    def find2(self, x):
        for i in range(len(self.st)-1, -1, -1):
            if self.st[i] == x:
                return i
        return -1

    # همه ایندکس های شامل (x) را برگرداند
    def find_all(self, x):
        result = []
        for i in range(len(self.st)):
            if self.st[i] == x:
                result.append(i)
        return result

    # جایگزینی تمام مقادیر x با y
    def replace(self, x, y):
        for i in range(len(self.st)):
            if self.st[i] == x:
                self.st[i] = y
 