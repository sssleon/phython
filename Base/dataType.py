a = b = c = 1
a, b, c = 1, 2, "john"
#�Ӻţ�+�����ַ���������������Ǻţ�*�����ظ�����
#Python�ַ���
str = 'Hello World!'
print str           # ��������ַ���
print str[0]        # ����ַ����еĵ�һ���ַ�
print str[2:5]      # ����ַ����е������������֮����ַ���
print str[2:]       # ����ӵ������ַ���ʼ���ַ���
print str * 2       # ����ַ�������
print str + "TEST"  # ������ӵ��ַ���

#Tulpe��Ԫ������һ���������ͣ����������¸�ֵ
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple               # �������Ԫ��
print tuple[0]            # ���Ԫ��ĵ�һ��Ԫ��
print tuple[1:3]          # ����ڶ�������������Ԫ�� 
print tuple[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinytuple * 2       # ���Ԫ������
print tuple + tinytuple   # ��ӡ��ϵ�Ԫ��

#List���б��� �������¸�ֵ
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list               # ��������б�
print list[0]            # ����б��ĵ�һ��Ԫ��
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