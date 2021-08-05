# https://programmers.co.kr/learn/courses/30/lessons/17681#

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        
        tmp = ""
        a = str(int(arr1[i])+ int(arr2[i]))
        if len(a) < n:
            a = '0'*(n-len(a)) + a
                
        for j in a:
            if j == '0':
                tmp += " "
            else:
                tmp += "#"
        answer.append(tmp)
    
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer