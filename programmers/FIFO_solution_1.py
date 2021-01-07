# 프로그래머스 LEVEL 2 프린터 문제 _other_codes
# 우선순위 큐 알고리즘
# 리스트 컴프리헨션 & any 함수

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)] #★
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): #★  ------> any에 비교연산자의 리스트 컴프리헨션 적용
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))