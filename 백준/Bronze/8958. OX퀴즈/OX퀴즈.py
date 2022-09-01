times = int(input())

for i in range(times):
    a = input()
    score = 0
    answer = 0
    for j in a:
        if j == "O":
            score += 1
        else:
            score = 0
        answer = answer + score
    print(answer)
