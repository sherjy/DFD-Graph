# Day1

###override重写

重写父类方法 覆盖

###overload重载

构造方法 有多个相同名字函数参数不同来区分

### POP&OOP

POP：面向过程编程

OOP：面向对象编程

AOP：面向切面编程 日志 事务管理 非原子操作

### 抽象类&接口类

比较抽象的东西放在抽象类中 水果 

```jing
所有类首字母都大写 默认空为NULL
java中的type有两种：引用类型 （有地址指向对象）基本类型(原始类型 8种)
引用类型首字母大写 String
原始类型 int 未初始化为0
bool 默认为false
```

静态变量 静态类型 类类型 static

局部变量 方法变量 必须在使用前初始化

Java中上一级类只能有一个

**extend:**

抽象类可以有实现的方法

```
abstract void drawcircle();
```

带括号的即为实现方法

```
abstract void drawcircle;
```

不带括号只声明 未实现

接口：百分百未实现

抽象类：至少有一个未实现

接口变量

```
final static ...
```

###面向对象三个特性

####继承

继承父类的属性和方法

虚调用 virtual invoke 设计模式

```
Fruit a=new Apple();
```

####封装

```
public ...
private ...
provide ...
```

**extend：**

内部类

```
public class LinkedList<T> {
    class Node {
        T data;
        Node prev;
        Node next;
    }

    Node fst;
    Node lst;
}
//高内聚
```

```
$ 文件名中带有dollar符号
```

外部类

先定义外部类才能定义内部类

####多态

通过重载实现多态

抽象类的方法一定是public方法

抽象类可以有实现的方法

String 是引用类型

###String与StringBuffer

```
String x1="aaa";
String x2="aaa";
String x3=new String("aaa");
//x1=x2/x1=x3.intern()
```

String 在传参数过程中

例如

```
public void String(s1){
    s1+="bbb";
}
```

会创造新的指向在main中定义的s1的实体并进行更改

StringBuffer在传参数过程中

例如

```
public void StringBuffer(s1){
    s1.append("bbb");
}
```

不会创造新的指向在main中定义的s1的实体 在原本的实体的s1上更改进行更改

###上溯与下溯造型

上溯相当于是常见的类型转换 小转大 默认可以

比如 苹果->水果

下溯是大转小 会提示异常 最好进行类型判断转换

比如 水果->苹果

###拆箱与装箱

```
Interger int 类型类
```

```
int x=10;
Interger y=x;
float z=10;
float z=10.0f;
```

~~float z=10.0;~~

###设计模式

单例模式

通过对构造函数重写来使得每个类只有一个实体

####线程不安全

```
public class SingletonDemo1 {
    private static SingletonDemo1 instance;
    private SingletonDemo1(){}
    public static SingletonDemo1 getInstance(){
        if (instance == null) {
            instance = new SingletonDemo1();
        }
        return instance;
    }
}
```

#### 线程安全

```
public class SingletonDemo2 {
    private static SingletonDemo2 instance;
    private SingletonDemo2(){}
    public static synchronized SingletonDemo2 getInstance(){
        if (instance == null) {
            instance = new SingletonDemo2();
        }
        return instance;
    }
}
```

#### 静态内部类

```
public class SingletonDemo5 {
    private static class SingletonHolder{
        private static final SingletonDemo5 instance = new SingletonDemo5();
    }
    private SingletonDemo5(){}
    public static final SingletonDemo5 getInsatance(){
        return SingletonHolder.instance;
    }
}
```

###Exception

异常通过

```
try{
...
}catch(){
...
	throw()

}finally{
...
}
来进行异常操作与处理
定义时注意throws ...
与打印信息的显示
```

###线程程序执行优先权

main的优先权默认为5

```
public class Main {
    public void setPrioritiesOnThreads() {
        Thread thread1 = new Thread(new TestThread(1));
        Thread thread2 = new Thread(new TestThread(2));
        thread1.start();
        thread2.start();
        try {

            //Wait for the threads to finish
            thread1.join();
            thread2.join();
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        System.out.println("Done.");
    }

    public static void main(String[] args) {
        new Main().setPrioritiesOnThreads();
    }
    class TestThread implements Runnable {
        int id;
        public TestThread(int id) {
            this.id = id;
        }
        public void run() {
            for (int i = 1; i <= 10; i++) {
                System.out.println("Thread" + id + ": " + i);
            }
        }
    }
}
```

join放置某处提前执行 插队操作

setPriorities设置优先权