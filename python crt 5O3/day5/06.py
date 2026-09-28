#selection sort
a=[5,7,2,11,17,16,14]
n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t

print(a)


