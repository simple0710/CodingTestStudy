# O(N + K)의 시간 복잡도
# 모든 값이 0보다 크거나 같다고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든범위를 포함하는 리스트 선언
cnt = [0] * (max(arr) + 1)

for i in range(len(arr)):
  cnt[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(cnt)):
  for j in range(cnt[i]): # 기록된 정보 출력
    print(i, end = ' ')