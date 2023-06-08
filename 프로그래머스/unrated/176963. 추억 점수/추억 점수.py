def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    for a,b in zip(name,yearning):
        score_dict[a] = b
        
    for case in photo:
        tmp = 0
        for i in range(len(case)):
            if case[i] not in score_dict:
                continue
            else:
                tmp += score_dict[case[i]]
        answer.append(tmp)
    return answer