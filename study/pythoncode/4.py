# 1
<<<<<<< HEAD
# num=0
# for i in range(2,101):
#     p=0
#     for j in range(2,i):
#         if i%j==0:
#             p=p+1
#     if p==0:
#         print(i,end=" ")
#         num=num+1
# print('\n%d'%(num))
# 2
# n=200
# for i in range(0,200):
#     if n%17==0:
#         print(n)
#         break
#     n=n-1
# 3
# m=1
# n=1
# while m<20000:
#     m=m*n
#     n=n+1
# n=n-1
# print(n)
# 4
# for a in range(1,31,):
#     for b in range(1,31):
#         for c in range(1,31):
#             if a*a+b*b==c*c:
#                 print(a,b,c)
# 5
# for i in range(100,1000):
#     if i*i%1000==i:
#         print(i)
# 6
# for i in range(1,101):
#     if i%7==0 and i%5!=0:
#         print(i)
# 7
# k=0
# j=7
# for i in range(1,5):
#         print(' '*k+'*'*j)
#         k=k+1
#         j=j-2

# for i in range(1,8,2):
#     print('*'*i)
# for i in range(5,0,-2):
#     print('*'*i)

# k=3
# j=1
# for i in range(0,3):
#     print(' '*k+'*'*j)
#     k=k-1
#     j=j+2
# k=0
# j=7
# for i in range(1,5):
#         print(' '*k+'*'*j)
#         k=k+1
#         j=j-2

# 习题
# 1
# flag='y'
# su=0
# num=0
# while flag!='n':
#     x=eval(input('please input a score:'))
#     su=su+x
#     num=num+1
#     flag=input('would you like to go on? y/n:')
# print('the average is %f'%(su/num))
# 2
# su=0
# while True:
#     x=eval(input('please input a number:'))
#     if x<0:
#         break
#     su=su+x
# print('the sum is %f'%(su))
# 3
# n=eval(input('please input a number:'))
# su=1
# for i in range(1,n+1):
#     su=su*i
# x=0
# for i in range(1,su+1):
#     x=x+1/i
# print('1+1/2+...＋1/(%d!)=%f'%(n,x))
# 4
# x=200
# for i in range(0,200):
#     if x%13==0:
#         break
#     x=x-1
# print('the number is %d'%(x))
# 5
# a=2
# s=0
# while a<=100:
#     s=s+a
#     a=a+2
# print('the sum is %d'%(s))
# 6
# num=6
# while True:
#     g=eval(input('please input a number'))
#     if g==num:
#         print('right!')
#         break
#     elif g>num:
#         print('bigger')
#     else:
#         print('smaller')
# 7
# x=1
# for i in range(0,9):
#     x=(x+1)*2
# print('total=%d'%(x))
#  8
# s=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=k and i!=j and j!=k:
#                 print(i,j,k)
#                 s=s+1
# print('total =',s)
# 9
# a=[2,6,7,3,9,1,4,7,90,34]
# t=0
# b=0
# for i in range(0,9):
#     t=a[i]
#     for j in range(i,10):
#         if a[j]<=t:
#             t=a[j]
#             b=j
#     a[b]=a[i]
#     a[i]=t
# print(a)
# 10
# def ch(n):
#     s=1
#     while n>0:
#         s=s*n
#         n=n-1
#     return s
# j=0
# for i in range(1,11):
#     j=j+ch(i)
# print('sum is %d'%(j))

=======
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
        
>>>>>>> b18fcbb52dc4f856ddbbf511e13d92fd97f1aecd
