#经典汉诺塔算法
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
#非递归汉诺塔算法
def com(a,b):  #用来判断应该从哪个柱子向另一个移动
    if len(a)==1 and len(b)==1:
        return
    elif len(a)==1:
        print(b[0],'-->',a[0])
        a.append(b.pop())
        return a,b
    elif len(b)==1:
        print(a[0],'-->',b[0])
        b.append(a.pop())
        return a,b
    elif a[-1]>b[-1]:
        print(b[0],'-->',a[0])
        a.append(b.pop())
        return a, b
    else:
        print(a[0], '-->', b[0])
        b.append(a.pop())
        return a, b

def move1(n):
    a=list(range(1,n+1))
    a.append('a')
    list.reverse(a)
    b=['b']
    c=['c']
    while 1:
        if a==['a'] and b==['b']:
            break
        elif n%2==0:
            if 1 in a:
                print('a --> b')
                b.append(a.pop())
                com(a,c)
            elif 1 in b:
                print('b --> c')
                c.append(b.pop())
                com(a,b)
            else:
                print('c --> a')
                a.append(c.pop())
                com(b,c)
        else:
            if 1 in a:
                print('a --> c')
                c.append(a.pop())
                com(a, b)
            elif 1 in b:
                print('b --> a')
                a.append(b.pop())
                com(b,c)
            else:
                print('c --> b')
                b.append(c.pop())
                com(a, c)

import time
time_start=time.time()
#move(21,'A','B','C')
move1(1n3)
time_end=time.time()
print('totally cost',time_end-time_start)
