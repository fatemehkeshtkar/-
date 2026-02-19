class DNode:
    def __init__(self, x):
        self.Data = x
        self.next = None
        self.back = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def del_after(self, x):
        """حذف گره بعد از اولین گره شامل x"""
        if self.head is None:
            print("error: list is empty")
            return
        current = self.head
        while current:
            if current.Data == x:
                if current.next:
                    node_to_delete = current.next
                    current.next = node_to_delete.next
                    if node_to_delete.next:
                        node_to_delete.next.back = current
                    del node_to_delete
                    return
                print("error: no node after", x)
                return
            current = current.next
        print("not found")

    def del_x(self, x):
        """حذف اولین گره شامل x"""
        if self.head is None:
            print("error: list is empty")
            return
        current = self.head
        while current:
            if current.Data == x:
                if current.back is None:
                    # حذف سر لیست
                    self.head = current.next
                    if self.head:
                        self.head.back = None
                    del current
                    return
                if current.next is None:
                    # حذف آخرین گره
                    current.back.next = None
                    del current
                    return
                # حذف گره وسطی
                current.back.next = current.next
                current.next.back = current.back
                del current
                return
            current = current.next
        print("not found")

    def display_forward(self):
        """نمایش لیست از ابتدا تا انتها"""
        current = self.head
        while current:
            print(current.Data, end=" <-> ")
            current = current.next
        print("None")

