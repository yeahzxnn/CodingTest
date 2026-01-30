import sys

n,m = map(int, sys.stdin.readline().split()) 

# 2. 도감 만들기 (두 가지 버전)
name_to_id = {}
id_to_name = {}

for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    name_to_id[name] = i
    id_to_name[i] = name

for _ in range(m):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        print(id_to_name[int(query)])
    else:
        print(name_to_id[query])