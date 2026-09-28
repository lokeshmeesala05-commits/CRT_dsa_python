# sum of primes till that number(including)
def isPrime(n):
    if n==1:
        return False
    if n==2:
        return True

    # for i in range(2,n):
    #     if(n%i==0):
    #         return False
    # return True

    i=2
    if n==3:
        return True
    while(i*i <= n):
        if(n%i==0):
            return False
        i+=1
    return True
        

def sumOfPrime(n):
    s=0
    for i in range(1,n+1):
        if isPrime(i):
            s+=i
    return s

print(sumOfPrime(2))        

  



