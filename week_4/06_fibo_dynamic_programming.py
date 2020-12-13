input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


# 1. memo 에 있으면 값 반환
# 2. 없으면 수식대로 구하고
# 3. 반환 전 메모에 기록 후 반환

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return fibo_memo[n]


print(fibo_dynamic_programming(input, memo))

"""
동적 계획법
1. 
2.

top down , Bottom up 뭔자 알자
"""