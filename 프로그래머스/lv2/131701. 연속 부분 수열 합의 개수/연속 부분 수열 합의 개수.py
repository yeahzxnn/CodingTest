from collections import deque

def solution(elements):
    answer = set()
    elements = deque(elements)
    
    for i in range(len(elements)):
        elements.rotate(1)
        for j in range(1, len(elements)):
            answer.add(sum(list(elements)[:j]))
        
    answer.add(sum(elements))
    return len(answer)