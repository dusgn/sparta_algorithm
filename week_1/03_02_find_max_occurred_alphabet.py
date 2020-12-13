# 각 알파벳의 빈도수를 alphabet_occurrence_list에 저장
# 각 문자열을 돌며 해당 알파벳인지 확인
# 알파벳을 인덱스화 시켜 알파벳의 빈도수를 업데이트

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
        else:
            continue
        alphabet_occurrence_array[index] += 1
        # 빈도수 배열이 생성됨

    max_occurrence = 0
    max_alphabet_index = 0
    # 빈도수 배열index 0- 25의 숫자와 max_ 와비교해 큰값을 교환해줌
    for index in range(len(alphabet_occurrence_array)):  # 0-25의 index 생성
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
            # 큰 값을 찾아 냄

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)
