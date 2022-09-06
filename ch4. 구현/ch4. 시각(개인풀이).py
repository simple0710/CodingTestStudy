n = int(input())

cnt = 0
# 시간, 분, 초를 반복문으로 구성
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 만약 3이 있다면 cnt += 1
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
