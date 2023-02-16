def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        target = sorted(array[i-1:j])
        answer.append(target[k-1])

    return answer