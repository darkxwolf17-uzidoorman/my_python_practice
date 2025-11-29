'''
示例：
输入: 5, 3
输出: 
和: 8
差: 2
积: 15
商: 1.67
'''
a, b=5, 6
print(a+b)  #加 输出11
print(a-b)  #减 输出-1
print(a*b)  #乘 输出30
print(a//b) #整除 输出0
print(a%b)  #除余 输出5
#除法 都输出0.83
#除法1
c = a/b
print(round(c, 2))
#除法2
print(f'{c:.2f}')
#除法3
print('{:.2f}'.format(c))
#除法4
print('%.2f' % c)
