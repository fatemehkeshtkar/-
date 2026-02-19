class Node:
    def __init__(self, d):
        self.Data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, x):
        """قرار دادن عنصر در ابتدای لیست"""
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, x):
        """قرار دادن عنصر در انتهای لیست"""
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, x, y):
        """قرار دادن y بعد از اولین گره شامل x"""
        if self.head is None:
            print("list is empty")
            return
        current = self.head
        while current:
            if current.Data == x:
                new_node = Node(y)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("not found")

    def insert_before(self, x, y):
        """قرار دادن y قبل از اولین گره شامل x"""
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.insert_first(y)
            return
        current = self.head
        while current.next:
            if current.next.Data == x:
                new_node = Node(y)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("not found")

    def display(self):
        """نمایش عناصر لیست"""
        current = self.head
        while current:
            print(current.Data, end=" -> ")
            current = current.next
        print("None")
