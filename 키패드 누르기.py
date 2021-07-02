# https://programmers.co.kr/learn/courses/30/lessons/67256/solution_groups?language=python3

def solution(numbers, hand):
    answer = ''
    
    pad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,"#"]]
    
    left = [0,3]
    right = [2,3]
    
    
    for i in numbers:
        if i in pad[0]:
            answer += 'L'
            left = [0, pad[0].index(i)]
        elif i in pad[2]:
            answer += 'R'
            right = [2, pad[2].index(i)]
        else:
            mid = [1,pad[1].index(i)]
        
            L = abs(left[0]-1) + abs(left[1]-mid[1])
            R = abs(right[0]-1) + abs(right[1]-mid[1])
            
            if L == R:
                if hand == 'left':
                    answer += 'L'
                    left = [1, mid[1]]
                elif hand == 'right':
                    answer += 'R'
                    right = [1, mid[1]]
            elif L < R:
                answer += "L"
                left = [1, mid[1]]
            elif L > R:
                answer += "R"
                right = [1, mid[1]]
    
    return answer