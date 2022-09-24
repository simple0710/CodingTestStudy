import sys
def binary_search(arr, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 중간 값이 타겟인 경우 1 반환
  if arr[mid] == target:
    return 1
  # 중간 값이 타겟보다 크다면 end = mid - 1
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid - 1)
  # 중간 값이 타겟보다 작다면 start = mid + 1
  else:
    return binary_search(arr, target, mid + 1, end)
n = int(input())
data1 = list(map(int, input().split()))
data1.sort()
m = int(input())
data2 = list(map(int, input().split()))

for i in data2:
  result = binary_search(data1, i, 0, n-1)
  if result == 1:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')