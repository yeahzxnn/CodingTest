import sys

n = int(sys.stdin.readline())

# 2. 숫자의 범위(1~10,000)만큼 빈 리스트 생성 (메모리 아끼기)
count_list = [0] * 10001
# 3. 숫자를 리스트에 담지 않고, 개수만 세기
for _ in range(n):
    num = int(sys.stdin.readline())
    count_list[num] += 1
# 4. 리스트를 돌며 개수만큼 출력하기
for i in range(10001):
    if count_list[i] != 0:
        for _ in range(count_list[i]):
            print(i)