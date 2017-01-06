# -*- coding: cp936 -*-
import time;

print time.time() #返回时间戳
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

import calendar
print calendar.month(2016,1)
