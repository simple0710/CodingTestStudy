def dfs(graph, v, visited):
    # 방문한 노드 True로 한다
    visited[v] = True
    print(v, end = ' ')
    # 방문한 노드와 연결된 노드의 연결 관계를 확인하고
    # 방문하지 않았다면 방문한다.
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)
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
dfs(graph, 1, visited)
