from collections import deque
def solution(cacheSize, cities):
    answer = 0
    #큐(캐시 만듦)
    cache = deque(maxlen=cacheSize)
       
    for city in cities:
        city = city.lower()
        
        #캐시 안에 도시가 있다면?(Hit)
        if city in cache:
            answer += 1
            # 기존 위치에서 지우고 맨 뒤로 다시 보내서 '최신 상태' 만들기
            cache.remove(city)
            cache.append(city)
            # 점수 +1
        #Miss
        else:   
            answer += 5
            cache.append(city)
    return answer