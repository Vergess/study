# 1
# s=input('please input a string')
# l=len(s)
# a=s.split()
# print('the length of the string is ',l)
# print('the word in the string is',len(a))
# 2
# i=0
# a=0;b=0;c=0;d=0;e=0
# while i<10:
#     score=eval(input('please input score  %d'%(i+1)))
#     if score>=90:
#         a=a+1
#     elif score>=80:
#         b=b+1
#     elif score>=70:
#         c=c+1
#     elif score>=60:
#         d=d+1
#     else:
#         e=e+1
#     i=i+1
# print('exce:%d,good:%d,normal:%d,pas:%d,bad:%d'%(a,b,c,d,e))
# 3
# dic={}
# i=0
# while i<10:
#     key=input('please input the name:')
#     value=eval(input('please input the score'))
#     dic[key]=value
#     i+=1
# dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
# print(dic)
# 4
# dic={'a':45,'b':78,'c':40,'d':96,'e':65,'f':90,'g':78,'h':99,'i':60,'j':87}
# l=len(dic)
# a=[];b=[]
# for key,value in dic.items():
#     a.append(key)
#     b.append(value)
# print(a)
# print(b)
# 5
# s=input('please input string')
# while len(s)!=0:
#     star=s[0]
#     num=s.count(star)
#     print('%s -> %d'%(star,num))
#     s=s.replace(star,' ')
#     s=s.strip()


# 1
# r=eval(input('please input a list'))
# for i in r:
#     print('the circle\'s area with the radius of %f is: %f'%(i,3.14*i*i) )
# 2
# a=eval(input('please input a 3*3 array'))
# for i in a:
#     for j in i:
#         print(j,end=' ')
#     print(' ')
# 3
# a=[1,2,3]
# b=[2,3,4]
# c1=[i for i in a if i in b]
# c2=[i for i in a if i not in b]
# print(c1)
# print(c2)
# 4
# import json
# stu=eval(input('please input a dict(input 1 choose the default)'))
# if stu==1:
#     stu={'name':'zhang san','sex':'male','age':'25'}
# stu1=json.dumps(stu)
# print(stu1)


    
