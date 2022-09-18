# O(N**2)의 시간 복잡도
# 보통은 삽입 정렬이 비효율적이나 
# 정렬이 거의 되어 있는 상황에서는 퀵 정렬 알고리즘보다 좋다.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    if arr[j] < arr[j - 1]: # 한 칸씩 왼쪽으로 이동
      arr[j], arr[j-1] = arr[j-1], arr[j]
    else: # 자기보다 작은 데이터를 만날 시에 멈춘다.
      break
print(arr)