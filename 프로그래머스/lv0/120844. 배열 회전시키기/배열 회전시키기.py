def solution(numbers, direction):
    answer = []
    if direction == "right":
        a = numbers.pop()
        numbers.insert(0, a)
        return numbers
    else:
        b = numbers[0]
        numbers.remove(b)
        numbers.append(b)
        return numbers