def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        free = chicken // 10
        chicken = chicken % 10
        
        answer += free
        chicken += free
    
    return answer