# L = [3,5]
# L[0:0] = [1,2]
# print(L)
# L[-1:-1] = [4]
# print(L)
# L[5:5] = [6]
# print(L)

# L[::] = L[-1::-1]   #这样不会改变id
# print(L)
# del L[-1]
# print(L)


# num1 = int(input("请输入第一个数:"))
# num2 = int(input('请输入第二个数：'))
# num3 = int(input('请输入第三个数：'))

# maxNum = max(num1,num2,num3)
# minNum = min(num1,num2,num3)
# aveNum = sum([num1,num2,num3])
# a = aveNum/3
# print('最大为：%d 最小值为：%d 平均值为：%d'%(maxNum,minNum,a))

# l = []
# while True:
#     num4 = int(input('请输入一个整数：'))
#     if num4 == 0:
#         break
#     else:
#         l.append(num4)
#     print(l)
#     zuidazhi = max(l)
#     zuixiaozhi = min(l)
#     if len(l) >=3:
#         pingjunzhi = sum(l)/3
#         print('最大值为：%d 最小值为：%d 平均值为：%d'%(zuidazhi,zuixiaozhi,pingjunzhi))
#     else:
#         print('最大值为：%d 最小值为：%d'%(zuidazhi,zuixiaozhi))
    
    
# begin = int(input('请输入一个开始值：'))
# end = int(input('请输入一个结束值：'))
# L1 = [x for x in range(begin,end) if x%2==0]
# print(L1) 

# L = []
# while True:
#     num5 = int(input('请输入一个数字：'))
#     if num5 == 0:
#         break
#     else:
#         L.append(num5)
#     print(L)
#     L1 = [x for x in L if x>0]
#     print(L1)
#     L2 = [x for x in L if x<0]
#     print(L2)

l1 = [x for x in range(1,100,3)]
print(l1)

l2 = '100,200,300,400,500'
a = l2.split(',')
l3 = [int(x) for x in a]
print(l3)

l4 = [[x,x+1,x+2] for x in range(1,8,3)]
print(l4)











