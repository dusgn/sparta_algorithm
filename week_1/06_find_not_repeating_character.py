input = "dljskff"


def find_not_repeating_character(string):
    temp = [0] * 26
    for char in string:
        index = ord(char) - ord('a')
        temp[index] += 1

    for num in range(len(temp)):
        if temp[num] == 1:
            return chr(num+ord('a'))
    return "_"


result = find_not_repeating_character(input)
print(result)