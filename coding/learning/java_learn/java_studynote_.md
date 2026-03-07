# java学习  

## java基础  

> 编程语言就是————计算机能够理解的一套特殊规则和词汇  
> 程序就是————一组命令，计算机会严格执行你下达的命令  

> 学习编程————就是学会这些能够操控计算机的咒语  

`System.out.println("机器人——人类的好朋友")`  

### main()方法  

程序可以由一个或多个文件组成，每个文件都包含函数分组的命令，在java中被称为方法，java中最小程序必须至少有一个方法，而且要从它开始执行，这个方法叫*main()*  

> main() 是程序的入口点。代码的执行从它开始。  

> 程序的执行顺序是至上而下、一行接一行的执行所有命令。当命令执行完成，程序就结束了。  

来看一个实际例子：  
```java  
public class HelloWorld {  
    public static void main(String[]args){  
        System.out.println("Hello World!");  
    }  
}  
```  

### 认识命令 System.out.println  

> **任何Java程序都是由一条条命令组成**  

* 每条命令的末尾要加上分号`;`  
* Java中区分大小写（除了SQL，其他编程语言都是区分大小写的）  

* *双引号* 文本内容需要在两侧用双引号包裹起来  
> 字符串一律使用标准的双引号 **`"`**  

命令：`System.out.println()`    
命令含义：在屏幕上打印内容，并在行尾加换行符  

命令：`System.out.print()`    
命令含义：在屏幕上打印内容，不加换行符  


### 认识变量  

*变量* 是一种用于存储数据的“容器”。Java中的所有数据都是通过*变量*来存储。  
> 变量就是一个普通的盒子  

变量有三个属性：  
* 类型: 整数、小数、文本、对象等  
* 名称: 只能包含字母数字下划线，且已字母开头  
* 值  

创建变量：先写类型，再写名称  
```java  
int a; // 创建一个名为*a*、类型为*int*的变量  
String s;  
double c;  
```  

赋值  
```java  
a = 1; // 将值 1 放入变量 a  
s = "java" // 将值 “java” 放入变量 s  

a = a + 1; // 将值 a + 1 的结果放入变量 a  
```  

创建变量并赋值  
```java  
int a = 5;  
int b = a + 1;  
String s = "I'm Amigo";  
```  


> ***重要！*** 同一个代码块中不能创建两个同名变量！  

### 注释  
> 会被编译器忽略，用于解释代码协助读代码之用  

* 单行注释 以双斜杠`//`开始，直到行尾。`//`之后的所有内容都会被视为注释，并会被编译器完全忽略。  
* 多行注释 以`/*`开始，以`*/`结束。之间的所有内容都是注释，可以跨越多行。  

```java  
int x = 42; // 程序员的年龄值  
// 初始化用户名变量  
String userName = "瓦夏"  

/*  
  这是一段多行注释  
  打印用户名  
*/  
System.out.println(userName);  
```  

> 注意：多行注释不能相互嵌套。  
> 其他常见用法：通过注释，禁用一行/多行代码  


### 数据类型  
#### int  
> int类型: 整数类型  

在java中int类型占用4个字节的内存。每个直接有8个byte组成，一个byte只能存放1/0，因此，int类型的取值范围大约是-20亿到+20亿  

* 创建int类型变量 `int x;`  
* 同时创建多个int类型变量 `int x, y, z;`  
* 赋值 `x = 5;`  
* 声明并初始化变量`int a = 5;`  
* 声明并初始化多个变量 `int x = 5, y = 6, z = 7;`  
* 整数运算 元算符号`+ - * / %`  
* **特殊**整数除法：在Java中，用整数除以整数，结果总是整数。余数会被丢弃。也可以说小数部分会被截断。  
* 整数取余`%` 返回的是整数除法的余数，而不是小数部分。（除不尽的那部分）  
* 自增与自减 `a++;` `a--;` (增加1 或 减少1）  
```java  
a = a + 1;  
a++; // 等同于 a = a + 1;  

a = a - 1;  
a--; // 等同于 a = a - 1;  
```  

#### 字符串与文本 String类型，字符串操作  

String类型是Java中使用最频繁最常用的类型之一。String对象自带很多方法。  


* 创建 `String name;`  
* 赋值 `name = "allinai";`  
* 连接（拼接）字符串 使用符号`+` `"String1" + "String2"`  
```java  
String name = "Anya";  
String city = "New York";  
String message = "Hello!" + city + name + city;  
```  
* 转义符`\` 如果字符串中包含一个双引号，就可以在其前面加上转义符  
    * `String quote = "he say: \"Hello\"";`  
    * \n 换行  
    * \t 制表符（缩进）  
    * `\\` 普通字符`\`  
    * `\"` 字符串内部的双引号  

* String内置方法  
    * str.length() 字符串长度  
    * str.toUpperCase() 转为大写  
    * str.toLowerCase() 转为小写  
    * str.trim() 去掉两端空格  
    > 字符串方法使用方式：`变量.方法()`  
    ```java  
    String name = "Andrey";  
    int length = name.length();  
    System.out.println(length);  
    ```  

    > **重要** 每个这样的方法都会返回一个新的字符串，原有字符串本身不会改变。  


#### 数据类型转换  

Java————是一种强类型语言  

* 将整数类型转换为字符串 `String.valueOf()`  
* 将字符串类型转换为整数 `Integer.parseInt()`  

```java  
int x = 5;  
String xString = String.valueOf(x);  

String a = "100";  
int aInt = Integer.parseInt(a);  
```  

|数据类型|占用内存大小字节|名称来源|  
|---|---|---|  
|byte|1|Byte,因为它占用一个字节的内存|  
|short|2|Short Integer|  
|int|4|Integer|  
|long|8|Long Integer|  
|float|4|Floating Point Number|  
|double|8|Double Float|  

> **重要** 变量的地址被认为是为其分配的内存块中第一个单元的地址。  

### 从键盘输入

与Python不同，java接收键盘输入数据的流程稍微麻烦。专有对象`System.in`一次只能读取一个字符。我们要借助类Scanner进行封装处理。

直接看代码：
```java
Scanner console = new Scanner(System.in); // 创建一个Scanner类，等待接收键盘输入。

String consoleString = console.nextLine(); // 读取字符串，强类型，需要先给变量声明数据类型String

int consoleInt = console.nextInt(); // 读取一个整数
double consoleDouble = console.nextDouble(); // 读取一个浮点数
```


## java基础-流程控制

> 流程控制是编程语言中比较核心的基础内容，因此单独列出

### 条件语句

运算符 `if else`
在Java中，通过条件语句，根据条件的真值执行不同的语句块。

```java
if (条件)
    命令1;
else
    命令2;
```

```java
int age = 17;
if (age < 18)
    System.out.println("You are small");
else
    System.out.println("You are old");
```

> **重要** 如果在条件成立或不成立时，需要执行多条语句，需要通过语句块来执行。
> 语句块：用大括号将多条语句包裹起来。
> 使用大括号，才能把多行代码放到同一个分支中，否则就会认为第二条及后面的语句非分支条件。Java中不会根据缩进来判断语句层级。`缩进只是为了看代码清晰`
> Java中根据`{}`来判断语句层级
> **建议** 始终写上大括号

```java
int temperature = 5;
if (temperature < 0)
{
    System.out.println("外面很冷");
    System.out.println("戴上帽子");
}
else if (temperature <= 5) // 条件组合 在多个选项中做出选择
{
    System.out.println("温度一般");
}
else
{
    System.out.println("暖和");
}
```

> **重要** Java中不要混淆不同类型的运算符！！！整数的运算符都只用到整数中！

整数比较运算符：
|比较运算符|含义|示例|
|---|---|---|
|==|等于|x == 5|
|!=|不等于|x != 5|
|>|||
|<|||
|>=|||
|<=|||


