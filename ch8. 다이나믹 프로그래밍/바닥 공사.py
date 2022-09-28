# 입력
# 3
n = int(input())

d = [0] * 1001

# 맨 처음의 경우와 다음 경우의 경우의 수
d[1] = 1
d[2] = 3

for i in range(3, n+1):
  d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])