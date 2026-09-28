s=[1,11,9,1,2,16,34]
k=3  #window size
n=len(s)
res=[]
for i in range(0,n-k+1):
    mx=0
    for j in range(i,i+k):
        if(s[j]>mx):
            mx=s[j]
    res.append(mx)        

print(res)    