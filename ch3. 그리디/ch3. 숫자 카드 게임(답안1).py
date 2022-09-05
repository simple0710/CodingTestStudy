#min() 함수 사용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    #가장 작은 수 지정
    min_value = min(data)
    #더 큰 값을 result로 둔다.
    result = max(result, min_value)
print(result)
