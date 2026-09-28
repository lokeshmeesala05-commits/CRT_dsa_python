# summation of sum of natural numbers for all digit in a given number 
n=int(input())
def summation(n):
    return n*(n+1)//2

sm = 0 

while(n > 0): 
    r = n % 10 
    sm += summation(r) 
    n = n // 10 

print(sm)