"""
링크드 리스트이 특징

next 만 알고 있기 때문에 다시 돌아가지 못한다.
어디가 끝인지 몰라서 뒤에서 k번째 노드를 찾기 쉽지 않음

A.
길이를 알아내자
한 바퀴 돌면서 길이를 알아낸 뒤 그 길이에서 k만큼을 뺀 순서의 노드를 반환하자

    def get_kth_node_from_last(self, k):
        length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur

B. 개선
그런데, 길이를 전부 알아야만 할까요?

2개의 포인터를 사용하면, 쉽게 해결할 수 있습니다!

k 만큼의 길이가 떨어진 포인터 두개를 두고, 한 칸씩 이동하면 어떨까요?
언젠가 앞에 나선 포인터가 끝에 도달하게 됩니다.
그 때 k 만큼 뒤떨어져있던 포인터는, 바로 끝에서부터 k 만큼 뒤떨어진 포인터가 됩니다!

             1   2  3 ....  k+1      끝
시작   : ㅁ← k 만큼의 길이 → ㅁ
1단계 :      ㅁ← k 만큼의 길이 → ㅁ
....
끝나면:                 ㅁ← k 만큼의 길이 → ㅁ

그런데, 과연 시간 복잡도 측면에서는 어떨까요?

둘다 결국 링크드 리스트의 끝까지 가야 하므로 같은 O(N) 의 성능을 가집니다.
게다가, 생각해보면 두 개의 공간값을 가지고 이동해야 하므로 비슷하게 연산량을 사용합니다.

따라서, 두 번 도는 것보다 한 번 도는 게 무조건 빠르다고는 생각 안하셨으면 좋겠습니다!
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
