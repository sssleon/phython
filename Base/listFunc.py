#!/usr/bin/python
# -*- coding: cp936 -*-

#list function
olist=['physics','chemistry',2000,1997]
samelist=['physics','chemistry',1997,2000]
difflist=[1,2,3,4,6,7]
del olist[2]                 #ɾ��ĳ��
print olist
print len(olist)             #����Ԫ�ظ���
if cmp(olist,samelist):      #�Ƚ��б�
    print "��ͬ"
if cmp(olist,difflist):
    print "����ͬ"
print max(olist)             #�����б�Ԫ�����ֵ
print min(olist)             #�����б�Ԫ����Сֵ

print olist.count(1997)      #ͳ��ĳ��Ԫ�����б��г��ֵĴ���
print olist.index(1997)      #���б����ҳ�ĳ��ֵ��һ��ƥ���������λ��

olist.append("2001")        #���б�ĩβ����µĶ���
olist.insert(0,'insert')    #����ָ��λ��
olist.extend(difflist)      #�����б�

print olist.pop()           #�Ƴ��б��е�һ��Ԫ�أ�Ĭ�����һ��Ԫ�أ������ҷ��ظ�Ԫ�ص�ֵ
olist.remove(6)             #�Ƴ��б���ĳ��ֵ�ĵ�һ��ƥ����
olist.reverse()             #�����б���Ԫ��
olist.sort()                #����

#Ԫ����б��໥ת��
aTuple = (123, 'xyz', 'zara', 'abc');
print list(aTuple)          #��Ԫ��ת��Ϊ�б�

aList=[1,2,3,4,5,6]
print tuple(aList)          #���б�ת����Ԫ��
#Ԫ��ֻ�����е�cmp,len,max,min����

#�ֵ�
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
print cmp(dict1,dict2)
print len(dict1)            #���Ϊ2
print str(dict1)            #�ַ�����ʽ���
print type(dict1)           #����ֵ�����
dict1.clear()               #����ֵ�
print dict1
dict3=dict2.copy()          #ǳ����
print dict3
bTuple=('name','age','sex')
dict4=dict.fromkeys(bTuple,10)  #�����ֵ䲢��Ĭ��ֵ
print dict4
print dict2.get('Sex','Nerver')#����ָ���ļ�ֵ���������򷵻�Ĭ��ֵ
print dict2.setdefault('Sex','Nerver')#��������Ѿ��������ֵ��У�������Ӽ�����ֵ��ΪĬ��ֵ
print dict2.has_key('Age')      #�ж��Ƿ��м�ֵ
print dict2.items()             #����������
print dict2.keys()              #��������Key
print dict2.values()            #��������Value
newdict={'Address':'aaa'}       
dict2.update(newdict)           #�����ֵ�
print dict2































