l=list(map(int,input().split()))

# for i in range(len(l)):
#     l[i]=l[i]*l[i]

# print(l)    





# res=[]
# n=len(l)
# sq=lambda x:x*x
# for i in range(n):
#     res.append(sq(l[i]))
# print(res)    


res=[]
sq=lambda x:x*x
# res=map(sq,l)     -->returns address <map object at 0x000001CF38EEB8E0>
res=list(map(sq,l))
print(res)