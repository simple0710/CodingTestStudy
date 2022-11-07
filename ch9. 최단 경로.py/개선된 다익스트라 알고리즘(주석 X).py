import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0, start)) # heapq.heappush(q, (start, 0))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q) # now, dist = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1] # cost = dist + i[0]
      if cost < distance[i[0]]: # if cost < distance[[i[1]]]
        distance[i[0]] = cost # distance[[i[1]]] = cost
        heapq.heappush(q, (cost, i[0])) # heapq.heappush(q, (i[1], cost))
        
dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])