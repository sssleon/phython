#!/user/bin/python
# -*- coding: UTF-8 -*-
# �ļ�����test.py

if True:
	print "Answer"
	print "True"
else:
	print "Answer"
	print "False"

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days	
item_one='1'
item_two='2'
item_three='3'
total = item_one + \
        item_two + \
        item_three
print total
word = 'word'
sentence = "����һ�����ӡ�"
paragraph = """����һ�����䡣
�����˶�����"""
print word,sentence,paragraph

#Ԫ������һ����������  ���������¸�ֵ
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple               # �������Ԫ��
print tuple[0]            # ���Ԫ��ĵ�һ��Ԫ��
print tuple[1:3]          # ����ڶ�������������Ԫ�� 
print tuple[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinytuple * 2       # ���Ԫ������
print tuple + tinytuple   # ��ӡ��ϵ�Ԫ��

#List���б� �������¸�ֵ
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list               # ��������б�
print list[0]            # ����б�ĵ�һ��Ԫ��
print list[1:3]          # ����ڶ�������������Ԫ�� 
print list[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinylist * 2       # ����б�����
print list + tinylist    # ��ӡ��ϵ���

#PythonԪ�ֵ�
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['one']          # �����Ϊ'one' ��ֵ
print dict[2]              # �����Ϊ 2 ��ֵ
print tinydict             # ����������ֵ�
print tinydict.keys()      # ������м�
print tinydict.values()    # �������ֵ
print tinydict['name']














