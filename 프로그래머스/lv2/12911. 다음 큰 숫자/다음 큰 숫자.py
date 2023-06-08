def solution(n):
    a = n+1
    while True:
        if bin(a).count('1') == bin(n).count('1'):
            return a
        a += 1