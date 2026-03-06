# Python 学习笔记

## 基础语法

### 基本数据类型

#### 基本数据类型

无论什么语言，都是有基本砖瓦组成，基本的砖瓦都对应着基本的数据类型

1. str（字符串）（通过成对的引号括起来标识为字符串）
2. int（整数）
3. float（浮点数）
4. bool（布尔值）（只有两个值）
    * True
    * False

#### 运算符

* 数学算术运算符 `+ - * / % // **`
* 数学比较运算符 `== != > >= < <=`
* 逻辑运算符 `and or not`
* 成员运算符 `in not in`
* 对象身份运算符 `is is not` 比较的是否是同一个对象
* 对象值比较运算符 `==` 比较的是两个对象的值是否相同
* None用is

##### 运算符优先级

括号最高！不确定就加括号！（工程第一原则）

#### 变量与赋值

* 变量命名规则只能包含字母数字下划线，字母打头
* 赋值：赋值符号`=` 将左边值 赋值给 右边变量名

```python
a = 1
b = 1.2
c = 'hello'
d = "ni hao"
e = True
f = False
a = "haha"
```

#### 注释

`#` 是注释符号，后面的内容都是注释，注解

```python
print("Hello World!") # 在控制台打印字符串: Hello World!
```

### 流程控制

什么是流程控制？流程控制就是控制代码按照什么顺序、在什么条件下执行。  

> python代码的默认执行顺序是从上到下

python中的流程控制主要靠4类语句完成：

1. 条件判断
2. 循环
3. 跳转控制
4. 异常流程

#### 条件判断

```python
if 条件判断:
    代码块 # 代码块要进行缩进
elif 条件判断2:
    代码块2
else:
    代码块3 # 其他条件都不符合的情况下执行else对应的代码块

# if语句可以单独使用
```

```python
if score >= 80:
    print("良好")
elif socre >= 60:
    print("及格")
else:
    print("不及格")
```

#### 循环控制

##### for循环

```python
for 变量 in 可迭代对象:
    代码块
```

```python
for i in [1, 2, 3]:
    print(i)

for i in range(10): # range(stop) 生成一个整数序列
    print(i)
```

##### while循环

```python
while 条件判断:
    代码块 # 1. 代码块缩进 2. 条件为真，代码块执行，再重新进行条件判断
```

```python
retry = 3
while retry > 0:
    print("重试")
    retry = retry - 1
```

##### 跳转控制

1. break 直接跳出循环/中断并退出循环/中止循环
2. continue 跳过本次循环
3. pass 占位，什么都不做

```python
for i in range(10):
    if i == 3:
        break

for i in range(5):
    if i == 2:
        continue
    print(i)

if condition:
    pass

```

##### 异常流程控制

```python
try:
    可能出错的代码
except 异常类型:
    出错后的处理
else:
    没出错后的处理
finally:
    一定会执行
```

```python
try:
    result = int(value)
except ValueError:
    result = None
```

### 数据结构

* list
* tuple
* set
* dict
* str
* None/bool

#### list 列表

python中 最重要的数据结构之一

list 是有序、可变、可重复的容器

特性：
* 有序
* 可重复
* 可修改
* 中括号标识

`a = [1, 2, 3]`

常见操作：
* 创建
```python
a = []
a = [1, 2, 3]
a = [i * 2 for i in range(5)]

a = list()
a = list(range(5))
a = list((1, 2, 3))
a = list("abc")
```

* 增
```python
lst.append(10)
lst.insert(1, "hello")
lst.extend([7, 8, 9])
lst + [100, 200]
```

* 删
```python
lst.remove("hello")
x = lst.pop(2)
del lst[1]
del lst[1:3]
lst.clear()
```

* 改
```python
lst[0] = 99
lst[1:3] = [10, 20]
lst.reverse()
lst.sort()
lst.sort(reverse=True)
new_lst = sorted(lst)
new_lst = lst.copy()
```

* 查
```python
lst[0]
lst[1:4]
3 in lst
lst.index("hello")
lst.count("hello")

# list的遍历
for x in a:
    print(x) # 普通遍历

for i, v in enumerate(a):
    print(i, v) # 带下标遍历
```

* 其他使用
```python
# 拷贝
a = [1, 2, 3]
b = a # 引用拷贝 a,b 指向同一个引用，列表没有任何变化

b = a.copy() # 浅拷贝 新增一个新列表，不过两个列表中的元素是相同的对象
b = a[:] # 浅拷贝

import copy
b = copy.deepcopy(a) # 深拷贝 a与b是两个完全独立的列表

```

* 常用内置函数
```python
len(a)
max(a)
min(a)
sum(a)
```

#### tuple 元组

tuple是不可变的有序容器，一旦创建，元素不能被增、删、改

* 基本创建
```python
t = (1, 2, 3) # 小括号标识元组
t = (1, ) # 创建单元素元素后面也要加逗号
t = tuple([1, 2, 3])
```

* 查
元组的查询同列表

* 常见用法
    1. 解包：`a, b = (1, 2)`
    1. 函数返回多个值，本质就是返回一个tuple
