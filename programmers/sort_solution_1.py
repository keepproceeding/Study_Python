
# 프로그래머스 LEVEL 2 가장 큰 수 문제 _other code★★★
# 정렬 알고리즘

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

x =[151,151,0]
solution(x)