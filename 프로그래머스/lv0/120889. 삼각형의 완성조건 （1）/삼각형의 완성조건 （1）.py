def solution(sides):
    answer = 0
    sides = sorted(sides)
    if sides[2] >= sides[0] + sides[1]:
        return 2
    else:
        return 1