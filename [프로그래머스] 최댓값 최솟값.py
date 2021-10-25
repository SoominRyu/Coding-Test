def solution(s):
    st = list(map(int,s.split()))
    answer = str(min(st))+' '+str(max(st))
    
    return answer
