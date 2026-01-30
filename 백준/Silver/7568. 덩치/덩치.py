import sys

# 1. 사람 수 N 입력 받기
n = int(sys.stdin.readline())
people = []

# 2. 몸무게와 키를 튜플로 묶어서 리스트에 저장
for _ in range(n):
    w,h = map(int, sys.stdin.readline().split())
    people.append((w,h))

# 3. 한 명씩 주인공(i)이 되어 다른 모든 사람(j)과 비교
for i in range(n):
    rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
            
    print(rank, end=' ')