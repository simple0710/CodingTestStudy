n = int(input())

data = list()
for _ in range(n):
  data.append(int(input()))
arr = sorted(data, reverse=True)

print(' '.join(map(str, arr)))