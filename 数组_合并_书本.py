#书本P39合并两有序序列




#做一个自定义函数是两个列表a和b实现相加合并输出

def sb(a,b):
    c=[]
    c=a+b
    for i in range(len(c)):
        for j in range(i,len(c)):
            if c[i]<c[j]:
                c[i],c[j]=c[j],c[i]
    return c





#------------------------------------------------------------------
from random import randint
a=[0]*20
b=[0]*15
c=[0]*35
a[0]=randint(95,100)
for i in range(1,20):
    a[i]=a[i-1]-randint(1,5)
b[0]=randint(95,100)
for i in range(1,15):
    b[i]=b[i-1]-randint(1,5)
print('原始数据序列一为：',a)
print('原始数据序列二为：',b)
print(sb(a,b))
"""
i=j=k=0
while(i<20 and j<15):
    if a[i]>=b[j]:
        c[k]=a[i]
        i+=1
        k+=1
    else:
        c[k]=b[j]
        j+=1
        k+=1
while i<20:
    c[k]=a[i]
    i+=1
    k+=1
while j<15:
    c[k]=b[j]
    j+=1
    k+=1
print('合并后的数据序列为：',c)"""
