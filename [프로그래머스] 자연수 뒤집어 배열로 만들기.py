def solution(n):
    n = list(map(int, str(n)))
    answer = []
    for i in reversed(range(len(n))):
        answer.append(n[i])
    return answer
