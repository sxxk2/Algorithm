def solution(a, b):
    m_d = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    for i in range(1, a):
        b += m_d[i]
    
    return ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"][b%7]