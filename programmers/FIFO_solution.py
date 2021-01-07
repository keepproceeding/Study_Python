# 프로그래머스 LEVEL 2 프린터 문제
# 우선순위 큐 알고리즘
def solution(priorities, location):
    x = list(zip(priorities,range(len(priorities))))  #--> ★zip을 한 후 리스트형태로 만들고 싶으면 반드시 zip함수 위에 list()를 해줘야한다!!!!!
    cnt = 0
    r = 0
    while x :
        for i in range(len(priorities)) :
            y = x.pop(0)
            if not x :
                cnt+=1
                answer = cnt
                break
            elif y[0] >= max(x)[0]:
                if y[1] == location :
                    cnt +=1
                    answer = cnt
                    r = 1
                    break
                else :
                    cnt +=1
            else :
                x.append(y)
        if r == 1:
                break
            
    return answer

priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))