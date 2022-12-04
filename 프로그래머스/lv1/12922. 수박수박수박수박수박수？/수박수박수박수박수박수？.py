def solution(n):
    answer = ''
    
    answer += ("수박" * ((n//2) + 1))[:n]
    
    return answer