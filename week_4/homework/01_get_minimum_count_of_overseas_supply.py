"""
조건 
1. 제일 큰 수량을 가져오면 된다? 그렇게 말고
    -> 재고가 바닥나기전 받을 수 있는 수량 중 가장 큰값을 받자

제일 많은 ? -> 정렬하자? 아니!
현재 재고의 상태에 따라 최고값을 받아야함( 동적임)
제일 많은 값만 가져가면 됨

1. 데이터를 넣을 때마다 최솟/ 최댓값을 동적으로 변경하며
2. 최소/최대값을 바로 꺼낼 수 있는 구조
-> HEAP!
"""
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    cur_day_idx = 0 # 현재 날짜를 알아야 재고 파악이 가능
    max_heap = []
    while stock < k : # k부터 정상화 되기 때문에
        for date_idx in range(cur_day_idx, len(dates)):
            print("date_idx=",date_idx)
            if dates[date_idx] <= stock:
                print("재고량보다 일수가 적음")
                heapq.heappush(max_heap, -supplies[date_idx])
                print(max_heap)
            else:
                print("재고량보다 일수가 커서 받기전에 공장 망한다")
                cur_day_idx = date_idx
                print("cur_day_idx=",cur_day_idx)
                break

        stock += -heapq.heappop(max_heap)
        answer += 1
        print("answer=",answer,"stock=",stock,"max_heap=",max_heap)

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))