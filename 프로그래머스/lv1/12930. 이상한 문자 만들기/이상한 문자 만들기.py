def solution(s):
    answer = ''
    s = s.split(" ")  

    for i in s:
        
        for j in range(len(i)):
            
            if not j % 2:
                answer += i[j].upper()
            else:
                answer += i[j].lower()

        answer += " "

    return answer[0:-1]
