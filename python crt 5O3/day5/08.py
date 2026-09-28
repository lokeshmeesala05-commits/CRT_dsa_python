s=[25,12,3,2,18,12]
k=3  #window size
n=len(s)
res=[]
for i in range(0,n-k+1):
    sm=0
    # for j in range(i,i+k):
    #     sm+=s[j]
    sm=sum(s[i:i+k])
    res.append(sm)        

print(res)    