from itertools import combinations  
from collections import Counter

#모든 경우의 수를 만들고 -> 하나만 뽑는다
def solution(orders,course):
    answer = []
    #course중 최대값 하나씩 찾아야하니까 필요
    for c in course:
        temp = []
        for order in orders:
            #정렬 -> 조합으로 모든 경우의 수 찾기
            temp += combinations(sorted(order),c)
            
        counter = Counter(temp)
        
        if counter:
            #제일 많이 주문된 것 뭐지?
            max_count = max(counter.values())
            if max_count >= 2:
                for menu,count in counter.items():
                    #제일 많이 주문된 것들 정답에 넣기
                    if count == max_count:
                        answer.append("".join(menu))
                
    return sorted(answer)