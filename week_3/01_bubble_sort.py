input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(i, n-1):
            if array[j] <  array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return

"""
n -i -1
-i = i번째 정렬마다 마지막이 정렬되어 반복하지 않아도 됨
-1 = j가 한 번씩 반복해 주지 않아도 됨
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
"""
bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!