# 프로그래머스 LEVEL 2 가장 큰 수 문제
# 정렬 알고리즘

def tuple(x) :
    answer = []
    for i in range(len(x)):
        answer.append(x[i][0])
    return answer

def solution(numbers):    
    if sum(numbers) == 0 :
        answer = '0'
        return answer
    numbers = list(map(str,numbers))
    temp = []
    for i in range(len(numbers)):
        temp.append((numbers[i],numbers[i]+numbers[i]+numbers[i]))
    temp = sorted(temp,key = lambda x : x[1][:4], reverse = True)

    answer = tuple(temp)
    return "".join(answer)
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
