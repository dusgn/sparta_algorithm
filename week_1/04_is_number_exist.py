input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:       #array의 길이만큼 연산 수행 N
        if number == element:   # 비교 연산 1번 실행
            return True         # N * 1 = N
    return False


result = is_number_exist(3, input)
print(result)
"""
운이 좋으면 한번에
운이 나쁘면 N만큼
알고리즘은 입력값의 분포에 따라 성능이 달라진다.
"""