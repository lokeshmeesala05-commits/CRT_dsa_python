l=[9,10,11,12,13,14,15]
for i in range(0,len(l)):
    print(l[i],":")
    for j in range(i+1,len(l)):
        print(l[j],end=" ")
    print()
