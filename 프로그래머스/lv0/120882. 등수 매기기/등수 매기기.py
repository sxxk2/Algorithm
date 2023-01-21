def solution(score):
    answer = []
    
    summed = []

    for i in score:
        summed.append(i[0]+i[1])

    for i in summed:
        answer.append(sorted(summed, reverse=True).index(i) + 1)

    return answer