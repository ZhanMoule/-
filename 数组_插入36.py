'''
实践操作一（数据为整数）:
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

#b=[i+randint(3,8) for i in range(0,100,10)]
#print(b)

x=randint(30,70)
print(x)

#先找位置再移动






# 边找位置边移动
# for 循环：




# while 循环：



