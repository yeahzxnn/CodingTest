def solution(numbers, hand):
    #변수
    answer = ""
    key_pos = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),
              7:(2,0),8:(2,1),9:(2,2),'*':(3,0),0:(3,1),'#':(3,2)}
    
    #초기 위치 설정
    left_pos = key_pos['*']
    right_pos = key_pos['#']

    for num in numbers:
    #1,4,7이 배열에 보일 경우, 무조건 L 출력
        if num in [1,4,7]:
            answer += "L"
            left_pos = key_pos[num]
    
    #3,6,9 배열에 보일 경우, 무조건 R 출력
        elif num in [3,6,9]:
            answer += "R"
            right_pos = key_pos[num]
    
    #2,5,8,0 -> 거리 계산 
        else:
            target = key_pos[num] #현재 위치
        
            dist_l = abs(target[0]-left_pos[0]) + abs(target[1]-left_pos[1])
            dist_r = abs(target[0]-right_pos[0]) + abs(target[1]-right_pos[1])
        
            if dist_l < dist_r:
                answer += "L"
                left_pos = target
            elif dist_l > dist_r:
                answer += "R"
                right_pos = target
            else:
                if hand == "left":
                    answer += "L"
                    left_pos = target
                else:
                    answer += "R"
                    right_pos = target
    return answer            