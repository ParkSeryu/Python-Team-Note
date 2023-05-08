# 순열(permutations) -> r개의 데이터를 뽑아 일렬로 나열하는 모든 경우
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2))  # 2개를 뽑는 모든 순열 구하기
print(result)

# 조합(combinations) -> r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

# product -> 같은 원소를 중복하여 뽑는 순열
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement -> 원소를 중복해서 뽑는 조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)