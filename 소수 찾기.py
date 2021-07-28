# https://programmers.co.kr/learn/courses/30/lessons/12921


# https://jokerldg.github.io/algorithm/2021/04/09/prime-number.html


# 내 답 = 오답

def solution(n):
    answer = []
    
    for i in range(2, n+1):
        prime = True
        
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                prime = False
                
        if prime:
            answer.append(i)
    return len(answer)

def solution(n):
    	# 2부터 n까지의 숫자 배열 만들기
    num_set = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num_set: # 배수 제거
            num_set -= set(range(i*2, n+1, i))
    answer = len(num_set)

    return answer