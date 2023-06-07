def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer

"""
def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
"""