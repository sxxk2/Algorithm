def solution(bin1, bin2):
    answer = ''
    
    answer = bin(int(bin1, 2) + int(bin2, 2))

    return answer[2:]