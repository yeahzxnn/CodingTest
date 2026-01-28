def solution(s):
    
    #길이가 1이면?
    if len(s) == 1:
        return 1
    
    results = []
    
    #for문은 배열 처음 문자와 같은 문자가 발견되면 멈춤.
    for step in range(1,len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        
        for j in range(step,len(s),step):
            curr = s[j:j+step]
            
            if prev == curr:
                count += 1
            else:
                compressed += (str(count)+prev) if count >= 2 else prev
                prev = curr
                count = 1
        
        compressed += (str(count)+prev) if count >= 2 else prev
        results.append(len(compressed))
        
    #가장 최소값 출력
    return min(results)