from audioop import mul


def solution(x, y):
    # Your code here
 
    step, m, f = 0, int(x), int(y)

    if m == 1 and f == 1:
        return str(step)

    while m > 0 and f > 0:

        if f > m:
            #If the difference between the two are large (5 times arbitrarily chosen)
            if f > 5*m:
                mul_factor = (int(f/m)-1)
                step += mul_factor
                f -= (mul_factor*m)
            else:
                f -= m
                step += 1
        else:
            #If the difference between the two are large (5 times arbitrarily chosen)
            if m > 5*f:
                mul_factor = (int(m/f)-1)
                step += mul_factor
                m -= (mul_factor*f)
            else:
                m -= f
                step += 1
        if solvable(m,f) is None:
            continue
        elif solvable(m, f):
            return str(step)
        else:
            return "impossible"
            
            
def solvable(m, f):
    if m == 1 and f == 1:
        return True
    elif m < 1 or f < 1 or m == f:
        return False
    else:
        return None

print(solution(4, 9))
print(solution(4,7))
print(solution(2, 1))
print(solution(10000, 1)) #mul_factor = int(10000/1) - 1 = 9999, add 9999 to step, subtract 9999 from m so it's one now
