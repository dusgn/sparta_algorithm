input = "011110"


# 모두 0으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_zero

# 모두 1로 만든느 방법에서 최소로 뒤집는 숫자
# count_to_all_one

# 1) 문자열이 뒤집어 질때, 카운트
# 2) 첫 번째 원소가 0인지 1인지에 추가해 주어야 함

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    if string[0] == '0':
        count_to_all_zero += 1
    elif string[0] == '1':
        count_to_all_one += 1
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_zero += 1
            if string[i + 1] == '1':
                count_to_all_one += 1
    print(count_to_all_one, count_to_all_zero)
    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

