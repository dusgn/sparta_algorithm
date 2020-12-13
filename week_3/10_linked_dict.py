"""
충돌 해결 A 체이닝
충돌된 인덱스를 링크드리스트로 연결해 줌
"""
class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        # .add("slow", "느린") -> [("slow", "느린)]
        # .add("fast", "빠른") -> [("slow", "느린), ("fast", "빠른")]
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        # 미리 배열을 담아 놓을 공간을 만들어 주어야 함
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())
            # -> [LinkedTuple(), LinkedTuple(),LinkedTuple(), ...]

    def put(self, key, value):
        # key를 해싱해 인덱스를 찾아야 함
        # 링크드 리스트 안에 key, value를 넣어 줌
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)