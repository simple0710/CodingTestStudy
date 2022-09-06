n = int(input())
x, y = 1, 1
plans = input().split()

# 각 움직임에 맞은 방향을 제시한다
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 움직임의 타입을 지정한다
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        # 해당 타입이 맞는 경우 그 움직임을 수행한다.
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #범위를 벗어난 경우는 넘어간다.
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
