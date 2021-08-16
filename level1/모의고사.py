# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]

    a1_m = 0
    a2_m = 0
    a3_m = 0

    for i in range(len(answers)):
        if a1[i%len(a1)] == answers[i]:
            a1_m += 1
        if a2[i%len(a2)] == answers[i]:
            a2_m += 1
        if a3[i%len(a3)] == answers[i]:
            a3_m += 1
    max_correct = [a1_m,a2_m,a3_m]

    for idx, i in enumerate(max_correct):
        if i == max(max_correct):
            answer.append(idx+1)
    return answer