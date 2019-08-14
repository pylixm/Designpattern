# -*- coding:utf-8 -*-
"""
抽象工厂

意图：
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

适用性：
一个系统要独立于它的产品的创建、组合和表示时。
一个系统要由多个产品系列中的一个来配置时。
当你要强调一系列相关的产品对象的设计以便进行联合使用时。
当你提供一个产品类库，而只想显示它们的接口而不是实现时。

理解：
- 抽象工厂，将工厂类创建产品的方法提取到接口，在客户端调用时，通过接口实例来调用该方法，从而达到实例化产品类目的。
这样只需修改，实例化“抽象”工厂实例时使用的具体工厂类即可。

- 对于python语言而言，没有接口，我们可以通过辅助类或者Duck Typing来聚合分支。

"""


class BaseUser(object):
    """
    user 基类
    """

    def Insert(self):
        pass

    def GetUser(self):
        pass


class SqlserverUser(BaseUser):
    """
    sql server 实现user类
    """

    def Insert(self):
        print("在SQL Server中给User表增加一条记录")

    def GetUser(self):
        print("在SQL Server中得到User表的一条记录")


class AccessUser(BaseUser):
    """
    Access实现的User
    """

    def Insert(self):
        print("在Access中给User表增加一条记录")

    def GetUser(self):
        print("在Access中得到User表一条记录")


class BaseFactory(object):
    """
    抽象工厂
    """

    def createUser(self):
        """ 子类需要实现 """
        pass


class SqlServerFactory(BaseFactory):
    """
    sql server工厂
    """

    def createUser(self):
        return SqlserverUser()


class AccessFactory(BaseFactory):
    """
    access工厂
    """

    def createUser(self):
        return AccessUser()

# 辅助类方式
# class DataAccess(object):
#
#     def connect(self, db_type='Sqlserver'):
#         self.db_type = db_type
#
#     def createUser(self):
#         if self.db_type == "Sqlserver":
#             return SqlserverUser()
#         elif self.db_type == "Access":
#             return AccessUser()


# Duck Typing
class DataAccess(object):

    def __init__(self, factory):
        self.factory = factory

    def createUser(self):
        return self.factory.createUser()


if __name__ == '__main__':
    # db = DataAccess()
    # db.connect()
    # user = db.createUser()
    # user.Insert()
    # user.GetUser()
    #
    # db.connect(db_type='Access')
    # user = db.createUser()
    # user.Insert()
    # user.GetUser()

    access = AccessFactory()
    db = DataAccess(access)
    user = db.createUser()
    user.Insert()
    user.GetUser()