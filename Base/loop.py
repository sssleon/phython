# -*- coding: cp936 -*-
#whileѭ��
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

#continue,break�÷�
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
    break   #����ѭ��
    num=raw_input("Enter a number:")        #��ȡ�����ֵ
    print "Your entered:",num

#for ѭ��
for letter in 'Phython':
    print letter
    
fruits=['banana','apple','mango']
for fruit in fruits:
    print fruit
    
for index in range(len(fruits)):    #len���س��ȣ�range��������
    print fruits[index]
    
for num in range(10,20):            #�������
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print '%d = %d * %d'%(num,i,j)
            break
    else:
        print num,'������'












    
