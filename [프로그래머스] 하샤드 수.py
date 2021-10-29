def solution(x):
    a = list(map(int,list(str(x))))
    sum = 0
    for i in a:
        sum += i
    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer
