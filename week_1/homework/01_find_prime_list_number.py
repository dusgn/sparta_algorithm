# input = 4
#
#
# def find_prime_list_under_number(number):
#     prime_num = list()
#     if number < 2:
#         return [number]
#     for num in range(2, number+1):
#         if num == 2 or num == 3 or num == 5:
#             prime_num.append(num)
#             continue
#         elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
#             continue
#         elif number % num == 0:
#             continue
#         else:
#             prime_num.append(num)
#
#     return prime_num
#
#
# result = find_prime_list_under_number(input)
# print(result)

# input = 20
#
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for n in range(2, number+1):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

# input = 20
#
#
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for n in range(2, number + 1):  # n = 2 ~ n
#         for i in prime_list:  # i = 2 ~ n-1
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)


input = 20

# 소수는 자기자신과 1외에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.

def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):  # n = 2 ~ n
        for i in prime_list:  # i = 2 ~ n-1
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)