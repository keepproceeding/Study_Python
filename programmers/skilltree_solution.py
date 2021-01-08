# 프로그래머스 LEVEL 2 스킬트리 문제
# skill_trees 목록에서 skill(먼저 배워야할 스킬트리)에 따라 가능한 스킬트리의 개수를 출력하는 함수
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees : 
        temp = []
        for j in skill : 
            temp.append(i.find(j))
        if temp.count(-1) != 0:
            if temp[-temp.count(-1):] == [-1]*temp.count(-1) and temp[:-temp.count(-1)] == sorted(temp[:-temp.count(-1)]):
                answer +=1
        else :
            if temp == sorted(temp):
                answer +=1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))