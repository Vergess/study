# 1
# import random
# num=random.randint(1000,9999)
# def mmm(num):
#     a=num//1000
#     b=(num-a*1000)//100
#     c=(num-a*1000-b*100)//10
#     d=(num-a*1000-b*100-c*10)
#     s=[a,b,c,d]
#     s.sort()
#     max=s[3]*1000+s[2]*100+s[1]*10+s[0]
#     min=s[0]*1000+s[1]*100+s[2]*10+s[3]
#     return max,min
# cha=0
# while cha!=6174:
#     (max,min)=mmm(num)
#     cha=max-min
#     print('%d - %d = %d'%(max,min,cha))
#     num=cha
# 2
# n=eval(input('please input n:'))
# print(' '*n,1)
# print(' '*(n-1),1,1)
# a=[1,1]
# for i in range(1,n):
#     b=[j for j in range(i+2)]
#     b[0]=1
#     b[-1]=1
#     for j in range(1,i+1):
#         b[j]=a[j-1]+a[j]
#     a=b
#     print(' '*(n-i-1),end=' ')
#     for m in b:
#         print(m,end=' ')
#     print(' ')  
# 3
# def yin(s):
#     b=[]
#     for i in range(1,s):
#         if s%i==0:
#             b.append(i)
#     return sum(b[:])
# r=[i for i in range(1,3001)]
# for i in r:
#     b=yin(i)
#     if i==yin(b):
#         r.remove(b)
#         print(i,b)
# 4
# n=eval(input('please input a number:'))
# def nn(n):
#     b=[]
#     for i in range(2,n):
#         flag=1
#         for j in range(2,i):
#             if i%j==0:
#                 flag=0
#         if flag==1:
#             b.append(i)
#     return b
# b=nn(n)
# for i in b:
#     for j in b:
#         for k in b:
#             if i+j+k==n and i>=j and j>=k:
#                 print('%d=%d+%d+%d'%(n,i,j,k))

# 1
# def su(num):
#     for i in range(2,num):
#         flag=0
#         if num%i==0:
#             flag=1
#         if flag==1:
#             return 0
#     return 1
# def re(num):
#     num=str(num)
#     j=0
#     z=0
#     for i in num:
#         z=z+int(i)*10**j
#         j=j+1
#     return z
# p=[i for i in range(2,101)]
# for i in p:
#     if su(i)==1 and su(re(i))==1:
#         print(i,end=' ')
# print(' ')
# 2
# num=eval(input('please input a number:'))
# print('%d ='%(num),end=' ')
# while num!=1:
#     for i in range(2,num+1):
#         if num%i==0:
#             num=int(num/i)
#             if num!=1:
#               print('%d *'%(i),end=' ')
#             elif num==1:
#               print('%d'%(i))
#             break


