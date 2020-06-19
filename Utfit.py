# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
file_name = 'Ut.xlsx'
df = pd.read_excel(file_name, sheet_name='Sheet1')
x = np.array(df.击穿时间)
y = np.array(df.电压峰值)


def fit_function(x, a, b, c):
    return 0.45 * (a + b / x**c) / 1000


[popt, pcov] = curve_fit(fit_function, x, y)
a = popt[0]
b = popt[1]
c = popt[2]
yval = fit_function(x, a, b, c)

plot1 = plt.plot(x, y, '*', label='original values')
plot2 = plt.plot(x, yval, 'r', label='fitted curve')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.legend(loc=1)
plt.title('U-t')
plt.show()
popt = ['{:.4f}'.format(i) for i in popt]
f = open('param.txt', 'w')
string1 = ['a = ', str(popt[0]), '\n', 'b = ', str(
    popt[1]), '\n', 'c = ', str(popt[2]), '\n']
for each in string1:
    f.writelines(each)
f.close()
