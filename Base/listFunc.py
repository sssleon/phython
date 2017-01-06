#!/usr/bin/python
# -*- coding: cp936 -*-

#list function
olist=['physics','chemistry',2000,1997]
samelist=['physics','chemistry',1997,2000]
difflist=[1,2,3,4,6,7]
del olist[2]                 #删除某项
print olist
print len(olist)             #返回元素个数
if cmp(olist,samelist):      #比较列表
    print "相同"
if cmp(olist,difflist):
    print "不相同"
print max(olist)             #返回列表元素最大值
print min(olist)             #返回列表元素最小值

print olist.count(1997)      #统计某个元素在列表中出现的次数
print olist.index(1997)      #从列表中找出某个值第一个匹配项的索引位置

olist.append("2001")        #在列表末尾添加新的对象
olist.insert(0,'insert')    #插入指定位置
olist.extend(difflist)      #插入列表

print olist.pop()           #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
olist.remove(6)             #移除列表中某个值的第一个匹配项
olist.reverse()             #反向列表中元素
olist.sort()                #排序

#元组和列表相互转换
aTuple = (123, 'xyz', 'zara', 'abc');
print list(aTuple)          #将元组转换为列表

aList=[1,2,3,4,5,6]
print tuple(aList)          #将列表转换成元组
#元组只有其中的cmp,len,max,min函数

#字典
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
print cmp(dict1,dict2)
print len(dict1)            #输出为2
print str(dict1)            #字符串形式输出
print type(dict1)           #输出字典类型
dict1.clear()               #清空字典
print dict1
dict3=dict2.copy()          #浅复制
print dict3
bTuple=('name','age','sex')
dict4=dict.fromkeys(bTuple,10)  #创建字典并附默认值
print dict4
print dict2.get('Sex','Nerver')#返回指定的键值，不存在则返回默认值
print dict2.setdefault('Sex','Nerver')#如果键不已经存在于字典中，将会添加键并将值设为默认值
print dict2.has_key('Age')      #判断是否有键值
print dict2.items()             #返回所有项
print dict2.keys()              #返回所有Key
print dict2.values()            #返回所有Value
newdict={'Address':'aaa'}       
dict2.update(newdict)           #更新字典
print dict2































