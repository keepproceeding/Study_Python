
def solution(s):
    answer = len(s)
    for i in range(1,(len(s)//2)+1):
        result = ''
        j=0
        cnt = 1
        while j<= (len(s)-i):
            if s[j:j+i] == s[j+i:j+2*i] :
                cnt += 1
                j += i
            elif cnt == 1 :
                result += s[j:j+1]
                j +=1
            else :
                result += str(cnt)+s[j:j+i]
                j +=i
                cnt = 1
        if j !=len(s) :
            result += s[j:len(s)]
        if answer > len(result) :
            answer = len(result)
        print(result)
        return answer

print(solution('aabbaccc'))
