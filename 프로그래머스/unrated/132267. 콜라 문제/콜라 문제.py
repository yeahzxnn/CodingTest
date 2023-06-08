def solution(a, b, n):
    answer = 0
    while(n>=a):
        rb = n%a #rb : 남아있는 병
        n = (n//a)*b
        answer += n
        n += rb
    return answer