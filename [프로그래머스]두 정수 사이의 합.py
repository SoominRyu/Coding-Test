def solution(a, b):
    answer = 0
    arr = [a,b]
    arr.sort()
    for i in range(arr[0],arr[1]+1):
        if a == b:
            answer = a
        else:
            answer += i
    return answer
