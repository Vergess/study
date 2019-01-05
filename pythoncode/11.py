#1
# import time
# import numpy as np
# time1=time.time()
# a=range(10000000)
# b=range(10000000)
# c=[]
# for i in range(len(a)):
#     c.append(a[i]+b[i])e
# time2=time.time()
# print(time2-time1)
# time3=time.time()
# c=np.arange(10000000)
# d=np.arange(10000000)
# e=c+d
# time4=time.time()
# print(time4-time3)

#2
from pandas import Series,DataFrame
# obj=Series([4,3,1,3])
# print(obj.index)
# data={'state':['hlp','hlp','hlp','fa'],
#        'year':[2001,2002,2003,2004],
#        'pop':[1,2,3,4]}
# print(DataFrame(data))