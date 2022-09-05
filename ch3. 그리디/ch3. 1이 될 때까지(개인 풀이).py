n, m = map(int, input().split())

cnt = 0
#1이 될 때까지 수행한다.
while n != 1:
    #n을 m으로 나누어 떨어지는지 확인한다.
    if n % m == 0:
        n //= m
        cnt += 1
    #안될 경우 -1을 수행한다.
    else:
        n -= 1
        cnt += 1
print(cnt)
    
