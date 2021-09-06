#  퀵 정렬 (파이썬 장점)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array):
  pivot = array[0]
  tail = array[1:]

  left = [x for x in tail if x <= pivot]
  right = [x for x in tail if x > pivot]

  return quick(left) + pivot + quick(right)

print(quick(array))
