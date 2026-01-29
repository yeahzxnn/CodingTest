#올바른 함수인지 판단
def is_correct(s):
    stack = 0
    for char in s:
        if char == '(': stack += 1
        else:
            stack -=1
            if stack < 0: return False
    return stack == 0
    
#뒤집어주는 함수
def flip_brackets(s):
    flipped = ""
    for char in s:
        if char == '(': flipped += ')'
        else: flipped += '('
    return flipped

def split_uv(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(': count += 1
        else: count -= 1
        if count == 0:
            return p[:i+1], p[i+1:]    

def solution(p):
    answer = ''
    
    #빈 문자열 처리
    if not p: return ""
    
    #u,v로 분리
    u, v = split_uv(p)
    
    #u가 올바른 괄호인가?
    if is_correct(u):
        #맞다면 u에 재귀 돌려서 v를 붙이면 됨
        return u + solution(v)
    
    #u가 올바른 괄호가 아닐경우?
    else:
        #지문에 적힌 것 수행
        answer = "(" + solution(v) + ")"
        #u의 앞뒤 떼고 방향반대?
        answer += flip_brackets(u[1:-1])
    return answer