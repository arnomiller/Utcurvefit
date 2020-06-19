# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:07:26 2020

@author: LYC
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def U_function(x,a,b,c):
    return 0.45 * (a + b / x**c) /1000

plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
file_name = 'curve_param.xlsx'
df = pd.read_excel(file_name)
param1 = list(df.param_ins)
param2 = list(df.param_90)
param3 = list(df.param_85)
param4 = list(df.param_80)
t = np.arange(1*10**-6,50*10**-6,0.1*10**-6)
Uins = U_function(t,param1[0],param1[1],param1[2])
U_90 = U_function(t,param2[0],param2[1],param2[2])
U_85 = U_function(t,param3[0],param3[1],param3[2])
U_80 = U_function(t,param4[0],param4[1],param4[2])

plot1 = plt.plot(t*10**6,Uins,'b',label='绝缘子')
plot2 = plt.plot(t*10**6,U_90,'g',label='90%长度间隙')
plot3 = plt.plot(t*10**6,U_85,'r',label='85%长度间隙')
plot4 = plt.plot(t*10**6,U_80,'c',label='80%长度间隙')
plt.ylabel('击穿电压/kV')
plt.xlabel('时间/μs')
plt.legend(loc=1)
plt.title('绝缘子与间隙的伏秒特性曲线')
plt.savefig('Ut_multi.png',dpi=300)
plt.show()