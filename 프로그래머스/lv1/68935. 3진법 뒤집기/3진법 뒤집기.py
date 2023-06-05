def solution(n):
    answer = 0
    arr = ""
    
    #3진법 바꾸기
    while n > 0:
        arr += str(n%3)
        n //= 3
    
    #문자열 반대로 정렬
    arr = arr[::-1]
    cnt = 1
    
    #다시 삼진법으로 계산
    for i in arr:
        answer += int(i) * cnt
        cnt *= 3
        
    return answer