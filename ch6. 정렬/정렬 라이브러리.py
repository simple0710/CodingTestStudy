# key의 활용
arr = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

result = sorted(arr, key = setting)
# result = sorted(arr, key = lambda x : x[1])
print(result)