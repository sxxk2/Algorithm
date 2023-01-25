def solution(dots):
    answer = 0
    x_li = []
    y_li = []
    
    for x, y in dots:
        x_li.append(x)
        y_li.append(y)
    
    answer += (max(x_li) - min(x_li)) * (max(y_li) - min(y_li))

    return answer