# 입력
# 4
# 1 3 1 5

n = int(input())
arr = list(map(int,input().split()))

d = [0] * n

d[0] = arr[0]
# 3 1 1 5 입력시 max로 처리 안하면 6이 나온다.
# 시작을 위한 빌드업이라 생각하자
d[1] = max(arr[0], arr[1]) 
for i in range(2, n):
  d[i] = max(d[i - 1], d[i-2] + arr[i])

print(d[n-1])