INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a][b] = c

# k 거쳐가는 노드, a는 출발하는 노드, b는 도착하는 노드
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print("INF", end = " ")
    else:
      print(graph[a][b], end = " ")
  print()
