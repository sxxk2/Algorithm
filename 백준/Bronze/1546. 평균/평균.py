n = int(input())
exam_list = list(map(int,input().split()))
max_score = max(exam_list)

new_list = []
for i in range(n):
    new_list.append(exam_list[i]/max_score*100)

print(sum(new_list)/n)