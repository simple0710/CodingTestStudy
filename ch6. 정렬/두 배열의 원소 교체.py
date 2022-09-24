# 입력
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# a는 오름차 순으로 정렬
# b는 내림차 순으로 정렬
a.sort()
b.sort(reerse=True)

# 맨 처음 인덱스부터 확인
for i in range(k):
  # b[i]가 더 크다면 스왑
  if a[i] < b[i]:
    a[i]. b[i] = b[i], a[i]
  # 같거나 작다면 종료
  else:
    break
# 출력
print(sum(a))
