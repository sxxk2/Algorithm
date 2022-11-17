def solution(x):
    answer = True
    a = 0

    for i in str(x):
        a += int(i)

    return x % a == 0