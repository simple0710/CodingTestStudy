import sys

input = sys.stdin.readline
n =  int(input())

LR = 1
UD = 1
move = list(map(str, input().split()))
# 해당하는 문자와 동일할 경우 조건문 수행
# +1인 경우는 넘어가지 않을 때 더하는 조건문
# -1인 경우는 0이 되지 않을 때 빼는 조건문
for i in move:
    if i == 'U':
        if UD - 1 > 0:
            UD += 1
    if i == 'D':
        if UD + 1 <= n:
            UD += 1
    if i == 'L':
        if LR - 1 > 0:
            LR -= 1
    if i == 'R':
        if LR + 1 <= n:
            LR += 1
  
print(UD, LR)
