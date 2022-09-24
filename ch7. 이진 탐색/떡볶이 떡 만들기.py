import sys
input = sys.stdin.readline

#덕의 개수와 요청한 떡의 길이
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력받기
data = list(map(int, input().rstrip().split()))

# 시작점과 끝점 설정
start = 0
end = max(data)

result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in data:
    # 떡을 잘랐을 때의 떡의 양 계산
    if x > mid:
      total += x - mid
  # 떡의 양이 부족한 경우 더 자르기(왼쪽 부분 탐색)
  if total < m:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
    start = mid + 1

print(result)