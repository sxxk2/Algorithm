def solution(hp):
    jg = hp // 5
    bj = (hp - jg * 5) // 3
    ig = (hp - (jg * 5) - (bj * 3)) // 1
    return jg + bj + ig