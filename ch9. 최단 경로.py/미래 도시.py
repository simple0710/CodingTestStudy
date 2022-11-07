INF = int(1e9)

n, m = map(int,input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 거쳐 갈 노드 x와 최종 목적지 노드 k 입력
x, k = map(int,input().split())
# k는 거쳐가는 노드, a는 출발 노드, b는 도착 노드
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      # 출발 노드및 도착 노드가 같다면 0
      if a == b:
        graph[a][b] = 0
      else:
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1번 노드에서 x를 거쳐 k로 가는 최단거리 ==
# 1번 노드에서 x까지의 최단 거리 + x에서 k까지의 최단 거리
distance = graph[1][k] + graph[k][x]
for i in graph:
  print(i)
if distance >= INF:
  print("-1")
else:
  print(distance)