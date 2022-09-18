# O(N**2) 시간 복잡도
# 10000개 이상이면 속도가 급격히 느려진다.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
  min_index = i
  for j in range(i + 1, len(arr)):
    if arr[min_index] > arr[j]:
      min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)