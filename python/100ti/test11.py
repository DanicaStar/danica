# -*- coding:utf-8 -*-
# @Time : 2020-11-02 18:02
# @Author: Danica
# @File : test11.py
f1 = 1
f2 = 1
for i in range(1,5):
    # print(f1,f2)
    print( '%12ld %12ld' % (f1,f2))
    # if (i % 3) == 0:
        # print('')
    f1 = f1 + f2
    f2 = f1 + f2