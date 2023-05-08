# 입력을 위한 전형적인 소스코드

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)


# n, m, k를 공백우르 구분하여 입력
n, m, k = map(int, input().split())

# input이 3, 5, 7 일시
# 3, 5, 7, 입력됨.
