# input() 메소드가 느려서 시관초과 날시
import sys

data = sys.stdin.readline().rstrip()
# 공백 문자를 제거하기 위해 관행적으로 .rstrip()를 사용한다.

print(data)