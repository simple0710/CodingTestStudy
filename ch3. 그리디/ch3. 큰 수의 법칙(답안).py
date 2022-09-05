n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    #first를 k번 더해준다.
    for i in range(k):
        #m이 0이면 종료
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    #두번째 수를 한 번 더해준다.
    result += second
    m -= 1
print(result)
