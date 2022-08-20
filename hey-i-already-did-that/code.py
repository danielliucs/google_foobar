def solution(n, b):
    #Your code here

    hashtable = {}

    k = len(n)
    idx = 0
    while True:

        x = getSortedN(n, False)
        y = getSortedN(n, True)

        x = convert_to_decimal(x, b) 
        y = convert_to_decimal(y, b)

        z = x -y

        n = convert_decimal_to_base(z, b)
        n = str(n).zfill(k) #Fill with leading 0's if necessary

        if n in hashtable:
            return (idx-hashtable[n])

        hashtable[n] = idx

        idx += 1
 

def getSortedN(n, ascending):
    num = str(n)
    
    if ascending:
        num = ''.join(sorted(num))
    else:
        num = ''.join(sorted(num, reverse=True))

    return num

def convert_to_decimal(base_number, b):
    if b == 10:
        return int(base_number)

    greatest_pow = len(base_number)-1
    ans = 0
    for i in base_number:
        dig = int(i)
        ans = ans + dig * pow(b, greatest_pow)
        greatest_pow -= 1

    return ans

def convert_decimal_to_base(decimal_number, b):
    if b == 10:
        return str(decimal_number)
    
    decimal_number = int(decimal_number)
    ans = ""

    while decimal_number != 0:
        ans = ans + str(int(decimal_number%b))
        decimal_number = decimal_number // b #one slash for python 2.7

    return ans[::-1]

if __name__ == "__main__":
   print(solution('1211', 10))
   print(solution('210022', 3))
   print(solution('1111', 2))