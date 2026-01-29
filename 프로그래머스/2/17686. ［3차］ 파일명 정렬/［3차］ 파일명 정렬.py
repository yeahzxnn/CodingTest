import re
def solution(files):
    
    #넣어둘 파일
    parsed_files = []
    
    for f in files:
        #HEAD,NUMBER나누는 것
        parts = re.split(r'(\d+)',f,1) #괄호
        
        #head,number정의
        head = parts[0]
        number = parts[1]
        
        #parsed_files에 어떻게 넣을지 -> append 사용
        #원본, lower로 만든 head, 숫자형 number넣어두기
        parsed_files.append((f, head.lower(),int(number)))
        
    #lambda활용해서 정렬 -> sort, key = lambda
    parsed_files.sort(key=lambda x:(x[1],x[2]))
    return [file[0] for file in parsed_files]