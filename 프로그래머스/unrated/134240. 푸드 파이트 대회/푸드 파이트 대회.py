def solution(food):
    answer = '0'
    
    for i in reversed(range(1, len(food))):
        b = str(i) * (food[i] // 2)
        answer = b + answer + b
    return answer