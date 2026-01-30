from collections import deque

def solution(cacheSize,cities):
    answer = 0
    
    #큐 -> 캐시 만들기
    cache = deque(maxlen=cacheSize)
    
    #LRU 
    #도시 수 만큼 도는 것
    for city in cities:
        city = city.lower()
        #city가 캐시 안에 있으면 hit
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
    return answer 