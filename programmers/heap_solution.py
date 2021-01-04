# 프로그래머스 LEVEL 2 더 맵게! 문제 -- heap q 알고리즘(heapq 모듈을 사용)

import heapq as hq
def solution(scoville, K):
    answer = 0
    cnt = 0
    hq.heapify(scoville)
    while True :
        if scoville[0] >= K:
            answer = cnt
            break
        elif len(scoville) == 1:
            answer = -1
            break
        else :
            x = hq.heappop(scoville)
            y = hq.heappop(scoville)
            z = x+2*y
            hq.heappush(scoville,z)
            cnt +=1
    return answer

scoville = [1,2,3,9,10,12]
K = 7

print(solution(scoville, K))