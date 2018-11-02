# seasons = {}
# seasons[1] = '春季有1，2，3月'
# seasons[2] = '春季有4，5，6月'
# seasons[3] = '春季有7，8，9月'
# seasons[4] = '春季有10，11，12月'
# print(seasons)
# num = int(input('请输入一个整数：'))
# if num in seasons:
#     print(seasons[num])
# else:
#     print('信息不存在！')
d = {}
strNum = input('请输入一段字符串：')
for x in strNum:
    if x in d:
        d[x]+=1
    else:
        d[x] = 1
print(d)



