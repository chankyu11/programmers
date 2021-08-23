# https://programmers.co.kr/learn/courses/30/lessons/81302
# https://www.youtube.com/watch?v=hCVgKE6qwFs

import queue

D = ((-1,0), (1, 0), (0, -1), (0, 1))

def bfs(place, row, col):
    visited = [[False for _ in range(5)]for _ in range(5)]
    q = queue.Queue()
    visited[row][col] = True
    q.put((row, col, 0))
    
    while not q.empty():
        curr = q.get()
        
        if curr[2] > 2:
            continue
        if curr[2] != 0 and place[curr[0]][curr[1]] == "P":
            return False
        
        # 방향
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
                
            if visited[nr][nc]:
                continue
                
            if place[nr][nc] == "X":
                continue
            visited[nr][nc] = True
            q.put((nr,nc,curr[2] + 1))
            
    return True
    

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if bfs(place, i, j) == False:
                    return False
    return True
            
    
def solution(places):
    answer = []
    
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer