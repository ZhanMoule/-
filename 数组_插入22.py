'''
实践操作（数据为整数）:
1. 创建含10个元素个数的数组a，存储9个数据的升序序列
2. 随机产生一个整数x
3. 将该数插入到适当位置，使序列依然有序
'''
from random import randint

a=[0]*10
a[0]=randint(1,10)
for i in range(1,9):
    a[i]=a[i-1]+randint(5,10)
print(a)

x=randint(20,50)
print(x)
'''
#先找位置再移动
for i in range(len(a)):
    if x<a[i]:
        break
print(i)

for j in range(len(a)-2,i-1,-1):
    a[j+1]=a[j]
    
a[i]=x 


# 边找位置边移动
# for 循环：
for i in range(len(a)-2,-1,-1):
    if x<a[i]:
        a[i+1]=a[i]
    else:
        a[i+1]=x
        break
else:
    a[0]=x
'''
# while 循环：

i=len(a)-1
while x<a[i-1]:
    a[i]=a[i-1]
    i-=1
a[i]=x


print(a)
