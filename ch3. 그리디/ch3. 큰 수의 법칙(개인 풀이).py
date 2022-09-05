import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

num_list = list(map(int,input().split()))
num_list.sort(reverse=True)
#가장 큰 값을 담은 리스트
new_list = list(num_list[0:2])

cnt = 0
ind = 0
result = 0
for i in range(m):
    result += new_list[ind]
    cnt += 1
    #한 번 더하고 다시 가장 큰 수를 더한다
    if ind == 1 :
        ind = 0
    #cnt가 k값과 같은 경우 두번째로 큰 수를 더한다.
    if cnt == k:
        ind = 1
        cnt = 0

print(result)
