def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

def series(n):
    if n<1:
        return 0
    else:
        return n + series(n-2)
   
def harmonic_sum(n):
    if n<2:
        return 1
    return 1/n + harmonic_sum(n-1)

def sum_digits_itr(num):
    sum = 0
    for n in str(num):
        sum += int(n)
    return sum

def sum_digits(num):
    num = str(num)
    if len(num)>1:
        return int(num[-1]) + sum_digits(num.replace(num[-1],""))
    return int(num[0])

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def pow(n,p):
    if p==0:
        return 1
    if p == 1:
        return n
    return n*pow(n,p-1)

    



"""
def sum_digits(num):
    if len(num)>1:
        print("cycle")
        return int(num.pop()) + sum_digits(num)
    return int(num[0])
"""
  
    
if __name__=='__main__':
    print(find_sum(10))
    print(series(7))
    print(harmonic_sum(6))
    print(sum_digits(1234567))
    print(fact(5))
    print(pow(5,0))