# 한 노드를 확인(True)하면 주변에 방문하지 않은 노드를 방문한다.
# 그러면 붙어있는 수로 넘어가도 False가 나오고 다음 방문하지 않은 노드를 방문한다.
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

result = 0
# 모든 노드에 대하여 음료수 채우기
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
