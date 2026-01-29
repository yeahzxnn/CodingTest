def solution(dirs):
    answer = 0
    #U,D,R,L 정의
    moves={'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    #현재 위치
    curr_x, curr_y = 0,0
    visited = set() #중복된 길 하나로 합쳐줌
    
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = curr_x + dx, curr_y + dy
        
        # 3. 경계 체크 (범위를 벗어나면 무시)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 4. "가본 길" 저장 (A->B와 B->A는 같은 길)
            visited.add((curr_x,curr_y,nx,ny))
            visited.add((nx,ny,curr_x,curr_y))
            
            curr_x, curr_y = nx, ny
            
        
    return len(visited) // 2