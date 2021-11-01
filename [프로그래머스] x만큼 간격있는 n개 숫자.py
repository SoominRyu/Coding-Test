def solution(x, n):
    answer = []
    ran = [x,x*n]
    
    print(ran)
    if x > 0:
        for i in range(ran[0],ran[1]+1,x):
            answer.append(i)
    elif x<0:
        for i in range(ran[0],ran[1]-1,x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
            
        
    return answer
