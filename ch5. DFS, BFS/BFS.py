from collections import deque

def bfs(graph, start, visited):
    # 큐 구현
    queue = deque([start])
    visited[start] = True
    while queue:
        # 큐에서 원소 하나를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph, 1, visited)