n = input()
x = int(n[1])
y = int(ord(n[0])) - int(ord('a')) + 1
# 그 자리에서 움직일 수 있는 방향 제시
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    # 움직일 수 있는 값을 더해본다
    nx = x + step[0]
    ny = y + step[1]
    # 움직일 수 있다면 result += 1
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        result += 1
print(result)
