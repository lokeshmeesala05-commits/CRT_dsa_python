L=[1,2,3,4,5,6,7]
l=0
r=len(L)-1
while(l<=r):
    if(l==r):
        print(L[l],end=" ")
    else:    
       print(L[l],end=" ")
       print(L[r],end=" ")
    l+=1
    r-=1