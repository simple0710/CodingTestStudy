n, m = map(int,input().split())

# n개의 화폐 단위 정보 입력
arr = list()
for i in range(n):
  arr.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * (m + 1)

# DP 진행 (보텀업)
dp[0] = 0
for i in range(n):
  for j in range(arr[i], m+1):
    if dp[j - arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
      dp[j] = min(dp[j], dp[j - arr[i]] + 1)

# 계산된 결과 출력
if dp[m] == 10001:
  print(-1)
else:
  print(dp[m])