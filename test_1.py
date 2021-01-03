def solution(participant, completion):
    for i in participant :
        if participant.count(i) != completion.count(i) :
            return i

print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))
