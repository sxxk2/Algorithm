def solution(n):
    answer = ''

    # if (n // 2) // 2:
    #     return "수박" * (n // 2)
    # else:
    #     return ("수박" * ((n // 2) +1))[:-1]
    
    answer += ("수박" * ((n//2) + 1))[:n]
    
    return answer