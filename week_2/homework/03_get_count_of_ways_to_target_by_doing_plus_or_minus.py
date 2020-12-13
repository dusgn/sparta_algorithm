"""
예제가 헷갈리기 쉬우니 좀 더 간단한 예제를 만들어 풀어보는 것도 방법
numbers = [2, 3, 1]
target_number = 0
이 문제는 모든 경우의 수를 다 해봐야지만 풀 수 있는 문제
일관적인 규칙을 찾을 수 없다.
1. +2 +3 +1 = 6         +++
2. +2 +3 -1 = 4         ++-
3. +2 -3 +1 = 0 # 타겟!   +-+
4. +2 -3 -1 = -2        +--
5. -2 +3 +1 = 2
6. -2 +3 -1 = 0 # 타겟!
7. -2 -3 +1 = -4
8. -2 -3 -1 = -6

뭔가 반복되어진다?
바로, 새로운 원소를 뺄지 더할지에 따라 방법이 추가된다는 걸 느낄 수 있다.

이를 함수로 작성해보면,
N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
N-1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 됩니다!

무슨 말이냐면,
[2, 3] 을 배치하는 모든 경우의 수에서
맨 마지막 원소인 1을 더하냐 빼냐에 따라서 [2, 3, 1] 의 경우의 수를 구할 수 있습니다.

[2, 3] 을 배치하는 모든 경우의 수는 아래와 같습니다.

1. +2 +3
2. +2 -3
3. -2 +3
4. -2 -3

여기서 1을 빼느냐 더하느냐에 따라 경우의 수가 다음과 같이 더 생깁니다.

1. +2 +3   → +1 = +2 +3 +1
                 → -1 = +2 +3 -1
2. +2 -3   → +1 = +2 -3 +1
                 → -1 = +2 -3 -1
3. -2 +3   → +1 = -2 +3 +1
                 → -1 = -2 +3 -1
4. -2 -3    → +1 = -2 -3 +1
                 → -1 = -2 -3 -1

즉 하나씩 원소를 추가할 때 마다 새로 추가된 원소를 더하고 빼는 경우의 수를 추가가

numbers = [2, 3, 1]
target_number = 0
result = []  # 모든 경우의 수를 담기 위한 배열


def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(numbers):  # 탈출조건!
        all_ways.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + numbers[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - numbers[current_index], all_ways)


get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
print(result)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
# 모든 경우의 수가 출력됩니다!
# [6, 4, 0, -2, 2, 0, -4, -6]

이렇게 모든 경우의 수를 다 구할 수 있었습니다!

그런데 저희는 모든 경우의 수를 구하는 것이 아니라,
모든 경우의 수가 target 과 일치하는지! 를 알고 싶은 거죠?
그래서 다음과 같이 코드를 변경합니다.

target 을 파라미터에 추가적으로 받아주고, all_ways 가 아니라 all_ways_count 를 알아야 하기 때문에 이렇게 변경합니다!
```python
numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum, all_ways_count):
    if current_index == len(numbers):  # 탈출조건!
        if current_sum == target:
            all_ways_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index],
                                                       all_ways_count)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index],
                                                       all_ways_count)

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0, result_count)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)

엇!! 그런데 result_count 가 0으로 찍힙니다!!

왜일까요?
그 이유는 바로 파이썬의 Call by Object Reference  라는 개념 때문에 그렇습니다.

함수에서 파라미터로 배열을 넘기면 그 내부에 원소를 추가하거나 할 수 있는데
파라미터로 int, str 타입의 변수를 넘기면 그 값이 복제되어 새로운 값을 생성합니다.

따라서 함수 내부의 all_ways_count 만 변경이 되고,
함수 외부의 result_count 는 변하지 않아서 문제가 생깁니다!

이런 경우에는, 함수 외부의 변수를 사용하기 위해
파이썬의 글로벌 변수라는 걸 사용하시면 됩니다!

외부에 정의되어 있는 변수를 내부에서 사용하기 위해서
global 변수이름 이라고 쓰기만 하면 됩니다!

all_ways_count 파라미터는 안 쓰니까 지워주면 되겠죠~!

numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):  # 탈출조건!
        if current_sum == target:
            global result_count
            result_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)  # 2가 반환됩니다!
"""

numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_count)