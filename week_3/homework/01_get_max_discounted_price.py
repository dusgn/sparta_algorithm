shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]
"""
최대로 할인 받으려면 어떻게 할까?
비싼 금액을 높은 할인률 받자
그럴려면 정렬하는게 좋겠당
배열.sort() 를 하면 오름차순 정렬
배열.sort(reverse=True) 내림차순 정렬
user_coupons 의 개수와 shop_prices 개수가 다를 수 있습니다!

따라서 아래와 같이 while 문과 인덱스를 사용해서 해결해야 합니다.

"""

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_idx = 0
    coupon_idx = 0
    max_discounted_price = 0

    while price_idx < len(prices) and coupon_idx < len(coupons):
        max_discounted_price += prices[price_idx] * (100 - coupons[coupon_idx]) / 100
        price_idx += 1
        coupon_idx += 1

    while price_idx < len(prices):
        max_discounted_price += prices[price_idx]
        price_idx += 1

    return int(max_discounted_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.