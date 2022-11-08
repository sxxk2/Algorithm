def solution(array):
    answer = []
    answer.insert(0, max(array))
    answer.insert(1, array.index(max(array)))
    return answer