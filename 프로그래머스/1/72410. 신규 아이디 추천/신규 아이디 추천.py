import re 

def solution(new_id):
   
    #First Round 치환 : 대문자 -> 소문자
    n = new_id.lower()
    
    #Second Round 제거 : 소문자,숫자,_,-,. 제외
    n = re.sub(r'[^a-z0-9\-_.]','',n)
    
    #Third Round 치환: 마침표 2번 이상 -> 하나의 마침표로 처리
    n = re.sub(r'\.+','.',n)
               
    #Fourth Round 치환: 마침표 처음이랑 끝에 있으면 제거
    n = n.strip('.')
    
    #Fifth Round 대입: new_id 빈 문자열 -> "a"대입
    if n == "":
        n = "a"
    
    #Six round 제거: 15개까지 허용, 제거 후 .가 처음과 끝에 있으면 제거
    if len(n)>=16:
        n = n[:15].strip('.')
    
    #Last: 2자 미만일 경우, 3자 이상이 될 때까지 끝 알파벳 추가
    while len(n) <=2 : 
        n += n[-1]

    return n