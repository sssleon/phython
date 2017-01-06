# -*- coding: cp936 -*-
#while循环
numbers=[1,2,3,4,5,6]
even=[]
odd=[]
while len(numbers)>0:
    number=numbers.pop()
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)
print even
print odd

#continue,break用法
i=1
while i<5:
    i+=1
    if i%2>0:
        continue
    print i
    
i=1
while 1:
    i+=1
    print i
    if i>5:
        break
    
while 1:
    break   #无限循环
    num=raw_input("Enter a number:")        #获取输入的值
    print "Your entered:",num

#for 循环
for letter in 'Phython':
    print letter
    
fruits=['banana','apple','mango']
for fruit in fruits:
    print fruit
    
for index in range(len(fruits)):    #len返回长度，range返回序列
    print fruits[index]
    
for num in range(10,20):            #输出质数
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print '%d = %d * %d'%(num,i,j)
            break
    else:
        print num,'是质数'












    
