import sys

def solution():
    #전부 대문자로 바꿔버리기
    s = sys.stdin.readline().strip().upper()
    #set으로 중복 피하기
    unique_s = list(set(s))
    
    counts = []
   
    for char in unique_s:
        cnt = s.count(char)
        counts.append(cnt) #알파벳 빈도수 저장
        
    max_cnt = max(counts) #빈도수 가장 많은 것중에 최대가 뭐야?
    
    #2이상이면 ? 출력(빈도수 같은 게 2개 이상이면)
    if counts.count(max_cnt) > 1:
        print("?")
    else:
        #최댓값 자리 있는 인덱스 자리 찾아야지?
        max_index = counts.index(max_cnt)
        #인덱스에 해당하는 알파벳 출력
        print(unique_s[max_index])
        
solution()