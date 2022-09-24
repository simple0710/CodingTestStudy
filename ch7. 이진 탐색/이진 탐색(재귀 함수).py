def binary_search(arr, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 값을 찾은 경우 인덱스 반환
  if arr[mid] == target:
    return mid
  # 타겟이 중간보다 작을 경우 end = mid - 1
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid - 1)
  # 타겟이 중간보다 클 경우 start = mid + 1
  else:
    return binary_search(arr, target, mid + 1, end)

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = binary_search(arr, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)