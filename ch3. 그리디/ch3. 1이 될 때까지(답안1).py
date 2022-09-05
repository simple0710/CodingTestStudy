n, k = map(int, input().split())
result= 0

while n >= k:
    #나누어 떨이지지 않는 경우 -1을 수행한다.
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
#마지막으로 남은 수에 -1 수행
while n > 1:
    n -= 1
    result += 1
print(result)
    
