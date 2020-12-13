"""
배열 정렬하는 방법
>이분탐색을 위한 전제조건 : 정렬!
파이썬은.sort() 를 이용하면 됨
정렬의 시간 복잡도는 배열의 길이가 N일 때
O(N * logN)

A. 배열을 가나다 순으로 정렬한 뒤 이진탐색 사용
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()  # menus 정렬!
    for order in orders:
        if not is_existing_target_number_binary(order, menus):
            return False
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)

이 방법의 시간복잡도는?
**한 발자국 더!**

우선, menus 를 정렬합니다.
menus 의 길이를 N 이라고 한다면 O(N * log N) 의 연산이 필요합니다.

그리고 정렬된 menus 내에서 이진 탐색의 시간 복잡도는 O(log N) 입니다.
이걸 orders의 개수 M 만큼 반복하게 되므로 O(M * logN) 의 연산이 필요합니다.

O(M * logN) * O(log N)
즉, O((M+N)*logn) 만큼의 시간 복잡도가 소요된다고 말할 수 있습니다!

이 문제는 단순히 특정한 문자열이 배열에 존재하는 지만 확인하면 된다.
정렬 필요 없이 집합 자료형을 사용하면 쉽게 해결이 가능하다.
! 집합은 중복을 허용하지 않는 자료형 !

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)

과연, 이 해결 방법의 시간 복잡도는 어떨까요?

menus 를 menus_set 으로 만들기 위해서는
orders 의 길이를 N 이라고 한다면 O(N) 의 연산이 필요합니다.

그리고 집합 내에서 탐색의 시간 복잡도는 O(1) 입니다.
이걸 주문의 개수 M 만큼 반복하게 되므로 O(M) 의 연산이 필요합니다.

즉, O(M+N) 만큼의 시간 복잡도가 소요된다고 말할 수 있습니다!
훨씬 효율적인 방법이 될 수 있다고 할 수 있습니다.

알고리즘에서 무조건 효율적인 방법은 없다.
이분탐색 언제든 효율적인 것은 아님!
상황에 따라 다른 자료구조를 사용하는 경우가 있음을 알자

"""
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)  #O(N)
    for order in orders:    # m
        if order not in menus_set: #O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
