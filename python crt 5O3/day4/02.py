l=[1,2,3,4,5,6]
print("using for:")
for i in range(len(l)):
    for j in range(len(l)):
        print(l[j],end=" ")
    print()    

print("using while:")
i=0
while i<len(l):
    j=0
    while j<len(l):
        print(l[j],end=" ")
        j+=1
    i+=1 
    print()   