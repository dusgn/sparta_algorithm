# input = "abcbaz"
#
#
# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n-1-i]:
#             return False
#     return True
#
#
# print(is_palindrome(input))

# 재귀함수의 목적은 문제를 점점 좁혀가는 것 // 내가 푼 것

input = "abba"


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))
