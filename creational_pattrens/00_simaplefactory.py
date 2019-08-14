# -*- coding:utf-8 -*-
"""
简单工厂

意图：
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。


理解：
将统一功能不同方式的类，聚合起来。封装了类的实现，使类的实例化变的简单。

"""


class Operation(object):
    """
    四则运算的父类,接收用户输入的数值
    """

    def __init__(self, number1=0, number2=0):
        self.num1 = number1
        self.num2 = number2

    def GetResult(self):
        pass


# 加法运算类
class OperationAdd(Operation):
    def GetResult(self):
        return self.num1 + self.num2


# 减法运算类
class OperationSub(Operation):
    def GetResult(self):
        return self.num1 - self.num2


# 乘法运算类
class OperationMul(Operation):
    def GetResult(self):
        return self.num1 * self.num2


# 除法运算类
class OperationDiv(Operation):
    def GetResult(self):
        if self.num2 == 0:
            return '除数不能为0 '
        return 1.0 * self.num1 / self.num2


# 其他操作符类
class OperationUndef(Operation):
    def GetResult(self):
        return '操作符错误'


# 简单工厂类
class OperationFactory(object):
    def choose_oper(self, ch):
        if ch == '+':
            return OperationAdd()
        elif ch == '-':
            return OperationSub()
        elif ch == '*':
            return OperationMul()
        elif ch == '/':
            return OperationDiv()
        else:
            return OperationUndef()


if __name__ == "__main__":
    ch = ''
    while not ch == 'q':
        num1 = int(input('请输入第一个数值:  '))
        oper = str(input('请输入一个四则运算符:  '))
        num2 = int(input('请输入第二个数值:  '))
        # Operation(num1,num2)
        OF = OperationFactory()
        oper_obj = OF.choose_oper(oper)
        oper_obj.num1 = num1
        oper_obj.num2 = num2
        print('运算结果为: ', oper_obj.GetResult())
        ch = input('退出请输入q:  ')
