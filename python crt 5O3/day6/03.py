#summation of cubesum of all digits in a number 
n=int(input())
sm = 0 
def cubeSum(num):
    return num*num*num
while(n > 0): 
    r = n % 10 
    sm += cubeSum(r) 
    n = n // 10 

print(sm)