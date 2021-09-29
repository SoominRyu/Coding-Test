def solution(n, lost, reserve):
    answer = 0

    len_r = len(reserve)
    len_l = len(lost)
    for i in lost:
      if i+1 in reserve:
        answer +=1
        reserve.remove(i+1)
      elif i-1 in reserve:
        answer +=1
        reserve.remove(i-1)
    return (n - len_l + answer)
