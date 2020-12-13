input = 5

# fibo(n) = fibo(n-1) + fibo(n-2)
# 탈출 조건  fibo(1) = fibo(2) = 1
def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765