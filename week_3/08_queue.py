class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 새로운 노드를 만듬
        # 큐가 비어있는지 확인
        # 비어있다면 최초의 노드가 head이자 tail이 됨
        # 비어있지 않다면 테일 노드 뒤에 새로운 노드를 추가
        # 테일에 새로운 노드를 추가해 줌
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        # 큐가 비어있는지 확인
        # head를 반환해줌
        # 포인터를 잃지 않게 삭제 헤드에 저장
        # 헤드에 다음 노드를 저장
        if self.is_empty():
            return " queue is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        # 큐가 비어있는지 확인
        # 맨 위, 즉 head 반환
        if self.is_empty():
            return " queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.is_empty())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())