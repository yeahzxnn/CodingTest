import re
def solution(files):
    #구분해서 넣을 파일 만들기
    parsed_files = []
    
    #파일에 넣을 거
    for f in files:
        parts = re.split(r'(\d+)', f, 1) #숫자 기준으로 짜르고, 숫자도 포함
        head = parts[0]
        number = parts[1]
        
        parsed_files.append((f,head.lower(),int(number))) #원본도 넣어야됨 f가 원본
       
    parsed_files.sort(key = lambda x:(x[1],x[2]))
    return [file[0] for file in parsed_files] #마지막에 원본으로 정렬