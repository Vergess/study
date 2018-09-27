# 1
num=0
for i in range(2,101):
    p=0
    for j in range(2,i):
        if i%j==0:
            p=p+1
    if p==0:
        print(i,end=" ")
        num=num+1
print(num)
        
