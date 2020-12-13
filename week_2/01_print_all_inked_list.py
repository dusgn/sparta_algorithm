class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node = Node(3)
# first_node = Node(4)
# node.next = first_node


# print(first_node)  # <__main__.Node object at 0x000001776D1BCD60>
# print(node.next)  # <__main__.Node object at 0x000001776D1BCD60>


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
