def solution(record):
    #record가 근데 문장 형태로 들어오잖아. 그러면 이걸 여기서 유저 id만 뽑아
    
    answer = []
    user_db = {}
    
    #Enter, Change
    for r in record:
        info = r.split()
        if info[0] in ["Enter", "Change"]:
            user_db[info[1]] = info[2]
    #Enter, Leave
    for r in record:
        info = r.split()
        if info[0] == "Enter":
            answer.append(f"{user_db[info[1]]}님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(f"{user_db[info[1]]}님이 나갔습니다.")
    return answer