# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
        
    en=['zero','one','two','three','four','five','six',
        'seven','eight','nine']
    answer = ''
    
    for idx,num in enumerate(en):
        if num in s:
            print(s)
            s=s.replace(num,str(idx))
        answer=s
    return int(answer)