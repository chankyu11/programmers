# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    length = len(s)
    
    if length%2 == 0:
        answer+= s[length//2-1:length//2+1]
    else:
        answer+= s[length//2]
        
    return answer