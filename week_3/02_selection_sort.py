input = [4, 6, 2, 9, 1]

"""
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx=j
        array[i], array[min_idx] = array[min_idx], array[i]
    return
    
            if array[i + j] < array[min_idx]:
                min_idx = i + j
        array[i], array[min_idx] = array[min_idx], array[i]    
"""
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(1, n-i):
            if array[i + j] < array[min_idx]:
                min_idx = i + j
        array[i], array[min_idx] = array[min_idx], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!