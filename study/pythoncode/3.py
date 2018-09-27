# 1
# num = eval(input('please input a number'))
# hour = num // 60
# min = num % 60
# print('hour is %f'% (hour))
# print('min is %f' % (min))
# 2
# x=eval(input('please input x'))
# if x<1000:
#     y=x
# elif x<2000:
#     y=0.9*x
# elif x<3000:
#     y=0.8*x
# else:
#     y=0.7*x
# print(y)
# 3
# x=input('please input a string')
# if x.isdigit():
#     print('the type of %s is number'%(x))
# elif x.isalpha():
#     print('the type of %s is alpha'%(x))
# else:
#     print('the type of %s is else'%(x))
# 4
# import math
# pi=math.pi
# x=input('pleasr input a number')
# if x.isdigit():
#     x=float(x)
#     area=x*x*pi
#     volume=pi*x*x*x*(4/3)
#     print('area is %.4f'%(area))
#     print('volume is %.4f'%(volume))
# else:
#     print('error!please input a number')


#　习题
# 1
# import math
# x1,y1=eval(input('please input x1,y1'))
# x2,y2=eval(input('please input x2,y2'))
# d=math.sqrt((x1-x2)**2+(y1-y2)**2)
# print('the distance is %f'%(d))
# 2
# x=eval(input('please input score'))
# if x>=90:
#     print('优秀')
# elif x>=80:
#     print('良好')
# elif x>=70:
#     print('中等')
# elif x>=60:
#     print('及格')
# else:
#     print('不及格')
# 3
# s=input('please input a string')
# l=len(s)
# num=0
# apl=0
# spa=0
# els=0
# for i in range(0,l):
#     if s[i].isdigit():
#         num=num+1
#     elif s[i].isalpha():
#         apl=apl+1
#     elif s[i]==' ':
#         spa=spa+1
#     else:
#         els=els+1
# print('there are %d numbers,%d aplha,%d spaces and %d other characters'%(num,apl,spa,els))
# 4
# import math
# a,b,c=eval(input('please input the eages'))
# if a+b>c and a+c>b and b+c>a:
#     p=(a+b+c)/2
#     t=p*(p-a)*(p-b)*(p-c)
#     area=math.sqrt(t)
#     print('the area is %f'%(area))
# else:
#     print('not trignale')