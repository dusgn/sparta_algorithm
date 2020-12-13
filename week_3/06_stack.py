class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 새로운 노드를 만들고 새노드에 헤드 위치를 넣어준다.
        # 그 뒤 현재 헤드를 새로운 노드로 덮어써준다.
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        # 스택에 반환할 값이 있는지 확인
        # pop을 쓰면 현재 헤드를 반환 하고 삭제한다.
        # 현재 헤드를 반환한다.
        # 현재 헤드의 다음 값을 현재 헤드에 덮어씐다.
        if self.is_empty():
            return " stack is empty "
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        # 스택에 반환할 값이 있는지 확인
        # 가장 꼭대기를 반환하면 됨
        if self.is_empty():
            return " stack is empty "
        return self.head.data   # self.head만 하면 노드 클래스가 나오니까

    # isEmpty 기능 구현
    def is_empty(self):
        # head가 None인지 검사하면 됨
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.pop().data)
print(stack.is_empty())