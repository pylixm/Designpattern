# -*- coding:utf-8 -*-
"""
工厂方法（简单工厂）

意图：
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。

理解：
拆分了工厂类，解决简单工厂的扩展修改问题，修改后只需要增加对于工厂类。
但是引入了新问题，
- 类的数量增多，代码量增多。
- 客户端调用的时候从传入标识变为需要调用具体的工厂类。

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


# 工厂类
class OperationFactory(object):

    def operation(self):
        pass


class AddOperationFactory(OperationFactory):

    def operation(self):
        return OperationAdd()


class SubOperationFactory(OperationFactory):

    def operation(self):
        return OperationSub()


class DivOperationFactory(OperationFactory):

    def operation(self):
        return OperationDiv()


class MulOperationFactory(OperationFactory):

    def operation(self):
        return OperationMul()


class UndefOperationFactory(OperationFactory):

    def operation(self):
        return OperationUndef()


if __name__ == "__main__":
    # 隐藏具体创建类(oper)的细节
    add = AddOperationFactory()
    oper = add.operation()
    oper.num1 = 1
    oper.num1 = 2
    oper.GetResult()