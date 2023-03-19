def solution(array, n):
    target = float("inf")
    idx = 0
    array.sort()
    
    for i in range(len(array)):
        diff = abs(array[i] - n)
        if diff < target:
            target = diff
            idx = i

    return array[idx]
