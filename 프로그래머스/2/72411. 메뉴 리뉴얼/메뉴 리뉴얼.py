from itertools import combinations
from collections import Counter

def solution(orders,course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order),c)
        
        counter = Counter(temp)
    
        if counter:
            max_counter = max(counter.values())
            if max_counter >= 2:
                for menu,count in counter.items():
                    if count == max_counter:
                        answer.append("".join(menu))
                
    return sorted(answer)