def solution(polynomial):
    answer = ''
    x_cnt = 0
    n_cnt = 0

    for i in polynomial.split():
        if i == "+":
            pass
        elif i == "x":
            x_cnt += 1
        elif "x" in i:
            x_cnt += int(i[:-1])
        else:
            n_cnt += int(i)

    if x_cnt:
        if x_cnt == 1:
            if n_cnt:
                answer += f"x + {n_cnt}"
            else:
                answer += f"x"
        else:
            if n_cnt:
                answer += f"{x_cnt}x + {n_cnt}"
            else:
                answer += f"{x_cnt}x"
    else:
        answer += f"{n_cnt}"

    return answer