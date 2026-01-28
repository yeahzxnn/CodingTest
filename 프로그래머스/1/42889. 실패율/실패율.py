def solution(N, stages):
    answer = {}
    #분모는 스테이지에 있는 사람들 수
    denominator = len(stages)
            
    for i in range(1,N+1):
        if denominator != 0:
            count = stages.count(i)
            answer[i] = count / denominator
            denominator -= count
        else:
            answer[i] = 0
    #내림차순으로 정렬 : dic에서 만들었던 실패율만 뽑아냄
    res = sorted(answer.items(), key=lambda x:x[1], reverse = True) 
    #스테이지만 뽑아서 이제 나열
    return [s[0] for s in res]