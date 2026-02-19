class DNode:
    def __init__(self, x):
        self.Data = x
        self.next = None
        self.back = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def ins_first(self, x):
        """قرار دادن عنصر در ابتدای لیست دوطرفه"""
        new_node = DNode(x)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.back = new_node
        self.head = new_node

    def ins_last(self, x):
        """قرار دادن عنصر در انتهای لیست دوطرفه"""
        if self.head is None:
            self.ins_first(x)
            return
        current = self.head
        while current.next:
            current = current.next
        new_node = DNode(x)
        current.next = new_node
        new_node.back = current

    def ins_after(self, x, y):
        """قرار دادن y بعد از اولین گره شامل x"""
        if self.head is None:
            print("error: list is empty")
            return
        current = self.head
        while current:
            if current.Data == x:
                if current.next is None:
                    self.ins_last(y)
                    return
                new_node = DNode(y)
                new_node.next = current.next
                current.next.back = new_node
                current.next = new_node
                new_node.back = current
                return
            current = current.next
        print("not found")

    def ins_before(self, x, y):
        """قرار دادن y قبل از اولین گره شامل x"""
        if self.head is None:
            print("error: list is empty")
            return
        current = self.head
        while current:
            if current.Data == x:
                if current.back is None:
                    self.ins_first(y)
                    return
                new_node = DNode(y)
                prev_node = current.back
                prev_node.next = new_node
                new_node.back = prev_node
                new_node.next = current
                current.back = new_node
                return
            current = current.next
        print("not found")

    def del_first(self):
        """حذف اولین گره"""
        if self.head is None:
            print("error: list is empty")
            return
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.back = None
        del temp

    def del_last(self):
        """حذف آخرین گره"""
        if self.head is None:
            print("error: list is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.back is None:
            self.del_first()
            return
        current.back.next = None
        del current

    def del_before(self, x):
        """حذف گره قبل از اولین گره شامل x"""
        if self.head is None or self.head.Data == x:
            print("error: no node before head")
            return
        current = self.head
        while current:
            if current.Data == x:
                node_to_delete = current.back
                if node_to_delete.back:
                    node_to_delete.back.next = current
                current.back = node_to_delete.back
                del node_to_delete
                return
            current = current.next
        print("x not found")

    def display_forward(self):
        """نمایش لیست از اول تا اخر"""
        current = self.head
        while current:
            print(current.Data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """نمایش لیست از انتها تا ابتدا"""
        current = self.head
        if not current:
            print("None")
            return
        while current.next:
            current = current.next
        while current:
            print(current.Data, end=" <-> ")
            current = current.back
        print("None")
