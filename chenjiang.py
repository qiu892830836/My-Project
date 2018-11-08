# #为了更好的保护属性安全，一般的处理是：将属性定义为私有属性；添加一个可以调用的方法供调用
# class People(object):
#     def __init__(self, name):
#         self.__name = name

#     def getName(self):
#         return self.__name

#     def setName(self, newName):
#         if len(newName) >= 5:
#             self.__name = newName
#         else:
#             print("error:名字长度需要大于或者等于5")
# p1 = People('小明')


# #在程序中，继承描述的是事物之间的所属关系
# class Cat(object):
#     def __init__(self, name, color="白色"):
#         self.name = name
#         self.color = color
#     def run(self):
#         print("%s--在跑"%self.name)

# # 定义一个子类，继承Cat类如下:
# class Bosi(Cat):
#     def setNewName(self, newName):
#         self.name = newName
#     def eat(self):
#         print("%s--在吃"%self.name)
# bosi =  Bosi('波斯猫')
# bosi.run()
# #私有的属性、方法，不会被子类继承，也不能被访问
# print(bosi.color)


# #多态
# #不同的类具有相同的实例方法名，返回值不同，将该方法提出来封装为一个接口
# #不同类的实例作为参数，传入该接口，得到不同返回值
# class F1(object):
#     def show(self):
#         print('F1.show')

# class S1(F1):
#     def show(self):
#         print('S1.show')

# class S2(F1):
#     def show(self):
#         print('S2.show')

# def fun(obj):
#     obj.show()


# #__str__方法 
# class MyNuber(object):
#     def __init__(self,value):
#         self.data = value
#     def __str__(self):
#         print('被调用')
#         return '数字%d'%self.data

