class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # 딕셔너리에 새로운 키와 값을 넣어줌

        # 키를 해싱 처리 후 값을 인덱스의 범위에 맞춘것을 index에 저장
        index = hash(key) % len(self.items)
        self.items[index]=value

    def get(self, key):
        # key 값에 따른 인자를 출력력

        # index를 키로 이용해 반환
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
