# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer = [-1]
            
            
            
    return sorted(answer)

# pythonic

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]