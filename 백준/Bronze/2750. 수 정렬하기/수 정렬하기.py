import sys

# 1. 숫자의 개수 입력 받기
n = int(sys.stdin.readline())
    
# 2. n개의 숫자를 입력받아 리스트에 저장 (정수로 변환 필수!)
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline())) #저장

# 3. 오름차순 정렬
numbers.sort()

# 4. 하나씩 출력
for num in numbers:
    print(num)