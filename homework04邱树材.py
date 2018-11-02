print('作业1')
i = 0
while i <= 10:
    print(i,end=' ')
    i += 0.5
print()
print('-'*50)
print()

print('作业2')
sum1 = 0
i = 1
while i <= 100:
    sum1 += 1/i
    i += 2
print('所有分数和为：%f'%sum1)
print('-'*50)
print()

print('作业3')
num = int(input('请输入三角形的宽度：'))
i = 1
while i <= num:
    print('*'*i)
    i += 1
print('-'*50)
print()

print('作业4')
height = int(input('请输入正方形的高度：'))

j = 1
while j <= height:
    i = j
    while i < height+j:
        print(i,end=' ')
        i += 1
    print()
    j += 1
    



