
#first solution but it's slow, can we do better
"""def solution(n):
    # Your code here
    n = int(n)
    if n <= 2:
        return n-1
    
    if n % 2 == 0:
        return 1+solution(n//2)

    return 1+min(solution(n-1), solution(n+1))"""

def solution(n):
    # Your code here
    """There is a recursive solution that is slow, optimize with bit operations"""
    n = int(n)

    steps = 0
    while n > 1:
        if n % 2 == 0: #if it's even (the lsb is 0)
            n //= 2
        elif n == 3 or n % 4 == 1: #if the two lsb are 01
            n -= 1
        else: #if the two lsb are 11
            n += 1
        steps += 1

    return steps


print(solution(15))