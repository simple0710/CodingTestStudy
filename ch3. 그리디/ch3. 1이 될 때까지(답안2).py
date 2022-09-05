n, k = map(int, input().split())
result= 0

while True:
    # 만약 n을 k로 나눌 수 있다면 result += 0, n = n이 성립된다.
    # 26, 3 기준
    # 만약 n을 k로 나눌 수 없다면 result += 2, n = 24가 성립된다.
    # 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼
result += (n - 1)
print(result)
