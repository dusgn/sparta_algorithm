"""
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for cha in string:
        if cha.isalpha():
            index = ord(cha) - ord('a')
        else:
            continue

        alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
"""
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
