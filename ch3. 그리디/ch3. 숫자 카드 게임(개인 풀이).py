n, m = map(int,input().split())

#카드를 나열한다
card_list = [list(map(int, input().split())) for i in range(n)]

result = 0

for i in range(n):
    #i행의 카드 값이 result보다 크다면 값을 바꾼다.
    if min(card_list[i]) > result:
        result = min(card_list[i])
print(result)
