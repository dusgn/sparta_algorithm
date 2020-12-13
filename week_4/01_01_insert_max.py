class MaxHeap:
    def __init__(self):
        # 왜 None? 배열로 구현하기 위해
        self.items = [None]

    def insert(self, value):
        # 1. 새 노드 맨 끝에 추가
        # 2. 새 노드 부모와 비교. 부모보다 크면 교체ㅔ
        # 3. 꼭대기 까지 반복
        self.items.append(value)
        cur_idx = len(self.items) - 1

        while cur_idx > 1:
            parent_idx = cur_idx // 2
            if self.items[cur_idx] > self.items[parent_idx]:
                self.items[cur_idx], self.items[parent_idx] = self.items[parent_idx], self.items[cur_idx]
                cur_idx = parent_idx
            else:
                break



max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!