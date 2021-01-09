# 프로그래머스 LEVEL 2 큰수 만들기 문제
# 이중 연결리스트 활용
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
        
def solution(number, k):
    temp = list(range(len(number)))
    n = 0
    t = 0
    answer = ''
    header_start = 0
    header_fin = 0
    
    for i in range(len(number)):
        temp[i] = Node(number[i],i-1,i+1)

    while True :
        if n == k:
            header_fin = len(number)
            break
        elif t == len(number)-1 :
            header_fin = len(number) - (k-n)
            break
        elif int(temp[t].data) >= int(temp[temp[t].next].data) :
            t = temp[t].next
        elif int(temp[t].data) < int(temp[temp[t].next].data):
            if temp[t].prev == -1:
                temp[temp[t].next].prev = -1
                header_start = temp[t].next
                t = temp[t].next
                n +=1
            else :
                temp[temp[t].next].prev = temp[t].prev
                temp[temp[t].prev].next = temp[t].next
                t = temp[t].prev
                n+=1

    t1 = header_start
    while True :
        if t1 == header_fin:
            break
        else :
            answer += temp[t1].data
            t1 = temp[t1].next
       
    return answer

number = "1924"
k = 2
print(solution(number,k))