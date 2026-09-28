l=[1,2,3,4,5,6]

print("left to right")
i=0
while(i<len(l)):
    print(l[i],end=" ")
    i+=1
print()
print("right to left")    
i=len(l)-1
while(i>=0):
    print(l[i],end=" ")
    i-=1
