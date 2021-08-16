# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for i in commands:
        tmp = array[i[0]-1: i[1]]
        tmp.sort()
        answer.append(tmp[i[2]-1])
    
    return answer

# pythonic

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
