# 1
# def su(num):
#     for i in range(2,num):
#         flag=0
#         if num%i==0:
#             flag=1
#         if flag==1:
#             return 0
#     return 1
# num=eval(input('please input a number:'))
# for i in range(2,num):
#     if su(i)==1 and su(num-i)==1:
#         print('%d=%d+%d'%(num,i,num-i))
#         break
# 2
# def com(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
# (a,b)=eval(input('please input two numbers:'))
# print('the bigger number is %d'%(com(a,b)))
# 3
# def su(n):
#     a=0
#     for i in range(1,2*n,2):
#         a=a+i
#     return a
# n=eval(input('please input n:'))
# print('the sum is %d'%(su(n)))
# 4
# def rep():
#     b=[1,2,3,-5,-4,5,9,-8,-1]
#     b.sort()
#     print(b)
# rep()

# 1
# a=0.63
# b1=0
# b2=0
# b3=0
# b4=0
# b1=int(a//0.25);a=a%0.25
# b2=int(a//0.1);a=a%0.1
# b3=int(a//0.05);a=a%0.05
# b4=int(a/0.01)
# print('need %d 0.25 coins,%d 0.1 coins,%d 0.05 coins,%d 0.01 coins'%(b1,b2,b3,b4))
# 2
# def swap(a,b):
#     if a<b:
#         t=a
#         a=b
#         b=t
#     print('after swap %d,%d'%(a,b))
# (a,b)=eval(input('please input a,b:'))
# swap(a,b)
# 3
# def p(y):
#     if y%400==0 or (y%4==0 and y%100!=0):
#         print('%d is a leap year!'%(y))
#     else:
#         print('%d is not a leap year!'%(y))
# y=eval(input('please input a year:'))
# p(y)
# 4
# def di(n):
#     if n<=1:
#         a=eval(input('please input a number'))
#         print(a)
#     else:
#         a=eval(input('please input a number'))
#         di(n-1)
#         print(a)
# di(5)