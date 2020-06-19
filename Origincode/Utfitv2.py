# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）


def fit_function(x, a, b, c):
    return 0.45 * (a + b / x**c) / 1000


def lsqfit(file_name):
    df = pd.read_excel(file_name, sheet_name='Sheet1')
    y = np.array(df.电压峰值)
    x = np.array(df.击穿时间)
    [popt, pcov] = curve_fit(fit_function, x, y)
    a = popt[0]
    b = popt[1]
    c = popt[2]
    yval = fit_function(x, a, b, c)
    return yval, popt, x, y


def plot_Ut(x, y, yval, file_name):
    plt.figure()
    plot1 = plt.plot(x*10**6, y, '*', label='original values')
    plot2 = plt.plot(x*10**6, yval, 'r', label='fitted curve')
    plt.ylabel('击穿电压/kV')
    plt.xlabel('时间/μs')
    plt.legend(loc=1)
    plt.title('伏秒特性曲线')
    plt.savefig(file_name, dpi=300)
    plt.show()


yval0, popt0, x0, y0 = lsqfit('Ut0.xlsx')
yval1, popt1, x1, y1 = lsqfit('Ut1.xlsx')
yval2, popt2, x2, y2 = lsqfit('Ut2.xlsx')
yval3, popt3, x3, y3 = lsqfit('Ut3.xlsx')


param1 = list(popt0)
param2 = list(popt1)
param3 = list(popt2)
param4 = list(popt3)
t = np.arange(1*10**-6, 50*10**-6, 0.1*10**-6)
Uins = fit_function(t, param1[0], param1[1], param1[2])
U_90 = fit_function(t, param2[0], param2[1], param2[2])
U_85 = fit_function(t, param3[0], param3[1], param3[2])
U_80 = fit_function(t, param4[0], param4[1], param4[2])
plt.figure(2)
plot1 = plt.plot(t*10**6, Uins, 'b', label='绝缘子')
plot2 = plt.plot(t*10**6, U_90, 'g', label='90%长度间隙')
plot3 = plt.plot(t*10**6, U_85, 'r', label='85%长度间隙')
plot4 = plt.plot(t*10**6, U_80, 'c', label='80%长度间隙')
plt.ylabel('击穿电压/kV')
plt.xlabel('时间/μs')
plt.legend(loc=1)
plt.title('绝缘子与间隙的伏秒特性曲线')
plt.savefig('Ut_multi.png',dpi=300)
plt.show()
