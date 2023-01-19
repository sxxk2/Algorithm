def solution(n):
    fac, i = 1, 1
    
    while True:
        if n < fac * i:
            return i - 1
        fac *= i
        i += 1
