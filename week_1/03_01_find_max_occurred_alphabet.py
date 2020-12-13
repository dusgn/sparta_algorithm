"""
input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alpha_arr =["a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x",
                "y", "z"]
    max_index = 0
    max_alpha = 0
    for char in alpha_arr:
        if max_index < string.count(char):
            max_index = string.count(char)
            max_alpha = char
        else:
            continue

    return max_alpha


result = find_max_occurred_alphabet(input)
print(result)
"""

#각 알파벳 마다 문자열을 돌며 몇 번 나왔는지 확인
#만약 그 수가 max보다 크면 값과 알파벳을 저장
input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alpha_arr = ["a", "b", "c", "d", "e", "f",
                 "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x",
                 "y", "z"]
    max_occurrence = 0
    max_alphabet = alpha_arr[0]

    for alphabet in alpha_arr:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)

