def solution(n):
    li = sorted(str(n), reverse=True)
    return int("".join(li))