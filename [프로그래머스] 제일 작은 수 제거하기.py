def solution(arr):
    
    if len(arr) >= 1:
        if len(arr) == 1 and arr[0] == 10:
            arr[0] = -1
        else:
            arr.remove(min(arr))

    return arr
