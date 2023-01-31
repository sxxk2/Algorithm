def solution(array):
    elements = {}
    
    for i in list(set(array)):
        cnt = array.count(i)
        
        if i in elements:
            pass
        else:
            elements[i] = cnt

    max_elements = [k for k,v in elements.items() if max(elements.values()) == v]
    
    if len(max_elements) > 1:
        return -1
    else:
        return max_elements[0]
