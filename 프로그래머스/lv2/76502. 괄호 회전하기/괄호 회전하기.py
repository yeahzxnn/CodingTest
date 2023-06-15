from collections import deque
def solution(s):
    
    flag = False
    count = 0
    stack = []
    queue = deque(s)
    
    for i in range(len(queue)):
        for el in queue:
            if el == '[' or el == '{'or el == '(':
                stack.append(el)
            else:
                if stack:
                    if stack[-1] == '[' and el == ']':
                        stack.pop()
                        flag = True
                    elif stack[-1] == '{' and el == '}':
                        stack.pop()
                        flag = True
                    elif stack[-1] == '(' and el == ')':
                        stack.pop()
                        flag = True
                        
        if flag and not stack: count += 1
        stack = []
        flag = False
        queue.append(queue.popleft())
    return count