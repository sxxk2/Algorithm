def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)

# for문을 활용한 풀이
#     answer = 1
#     for i in box:
#         answer *= i // n
#     return answer