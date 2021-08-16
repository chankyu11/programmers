# https://programmers.co.kr/learn/courses/30/lessons/12930#


def solution(s):
    answer = []
    
    for i in s.split(" "):
        tmp = ''
        for j in range(len(i)):
            
            if j % 2 == 0:
                tmp += i[j].upper()
            else:
                tmp += i[j].lower()
            
        
        answer.append(tmp)
                
    return " ".join(answer)