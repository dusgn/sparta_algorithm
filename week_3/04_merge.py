array_a = [1, 2, 3, 4]
array_b = [5, 6, 7, 8]


def merge(array1, array2):
    array_c = []
    array1_idx = 0
    array2_idx = 0
    while array1_idx < len(array1) and array2_idx < len(array2):
        if array1[array1_idx] < array2[array2_idx]:
            array_c.append(array1[array1_idx])
            array1_idx += 1
        else:
            array_c.append(array2[array2_idx])
            array2_idx += 1

    if array1_idx == len(array1):
        while array2_idx < len(array2):
            array_c.append(array2[array2_idx])
            array2_idx += 1
    if array2_idx == len(array2):
        while array1_idx < len(array1):
            array_c.append(array1[array1_idx])
            array1_idx += 1
    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!