def solution(quiz):
    answer = []

    for i in quiz:
        q, a = i.split("=")
        res = eval(q)
        
        if res == int(a):
            answer.append("O")
        else:
            answer.append("X")

    return answer