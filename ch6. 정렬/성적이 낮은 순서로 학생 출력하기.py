n = int(input())

data = list()
for _ in range(n):
  si = input().split()
  data.append((si[0], si[1]))
data = sorted(data,key = lambda x : x[1])

for name in data:
  print(name[0], end = ' ')
