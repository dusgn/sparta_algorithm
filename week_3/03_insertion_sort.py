input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            else:
                break
                #작지 안다면 앞은 다 정렬된 상태이기 떄문에 더 비교할 필요X
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!