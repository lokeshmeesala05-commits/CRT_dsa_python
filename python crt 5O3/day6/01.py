#sum of factorials in a given digit
def factorial(n): 
    fact = 1 
    i = 1 
    while(i <= n): 
        fact = fact * i 
        i += 1 
    return fact 

n = int(input()) 
sm = 0 

while(n > 0): 
    r = n % 10 
    sm += factorial(r) 
    n = n // 10 

print(sm)
