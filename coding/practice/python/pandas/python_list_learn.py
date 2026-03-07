# 列表推导式学习

l = [] # 定义一个空列表

def my_func(x):
    """这是一个简单的函数，接受一个参数x，并返回x的两倍。"""
    return x * 2

for i in range(5):
    l.append(my_func(i)) # 将函数的返回值添加到列表中

print(l) # 输出列表

# 列表推导式
# 列表推导式就是一种简洁的语法，用于创建新的列表。它可以用来替代传统的for循环和if语句来生成列表。
# 语法格式： [expression for item in iterable if condition]
# 其中，expression是生成新列表元素的表达式，item是从iterable中取出的元素，condition是一个可选的条件表达式，用于过滤元素。
# 例如，下面的代码使用列表推导式生成一个包含0到9的平方的列表：
squares = [x**2 for x in range(10)]
# print(squares) # 输出平方列表

l = [my_func(x) for x in range(5)] # 使用列表推导式生成一个新的列表
print(l) # 输出列表

# 列表推导式还支持多层嵌套，第一个for循环为外层循环，第二个for循环为内层循环：
l = [m + "_" + n for m in ['A', 'B'] for n in ['c', 'd']]

print(l) # 输出列表

# 第二个语法糖
# 带有if选择的条件赋值
# 形式： value_if_true if condition else value_if_false

value = 'cat' if 2>1 else 'dog' # 根据条件选择值

print(value) # 输出 'cat'

# 等价：
a, b = 'cat', 'dog' # 定义两个变量
condition = 2 > 1 # 定义条件
if condition:
    value = a # 如果条件为真，赋值为a
else:
    value = b # 如果条件为假，赋值为b
print(value) # 输出 'cat'

# 综合实例：
# 列表推导式 + if条件赋值

# 需求名称： 截断列表中超过5的元素，超过5的用5替代，小于等于5的元素保持不变。

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 定义一个列表
l = [i if i <= 5 else 5 for i in l] # 使用列表推导式和条件赋值生成一个新的列表
print(l) # 输出列表