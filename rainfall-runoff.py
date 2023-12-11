
import math
import sys
import pandas as pd
import csv
import os
import numpy as np
# import matplotlib.pyplot as plt
from numpy import double
#需要知道该流域的形心

data = pd.read_csv(r'E:\data\keke\ex120101GPM.csv', encoding='gbk')
T_sum = []
Q_sum = []
Qn_sum = []
Mw_sum = []
Ms_sum = []
time_sum = []
time = 0
for i in range(len(data)):
    time = time + 1
    F, L, J, H10P, H60P, H360P, S, Dens, Du =data.iloc[i][1:]
    n = 1 + (1.285 * (math.log((H10P / H60P), 10)))
    k = 3 / (4 - n)
    miu = 3.6 * (np.power(F, (-0.19)))
    cita = L / (np.power(J, 1 / 3) * np.power(F, 1 / 4))
    m = (np.power(cita,0.204))*0.221
    tao_0 = (pow(0.278, k)) / (pow((m * pow(J, 1 / 3) / L), 4 / (4 - n)) * pow((S * F), (1 / (4 - n))))
    print(n)
    print(miu)
    tao_c = pow(((1 - n) * S / miu), (1 / n))
    fai = pow(((tao_0 / tao_c)* (pow(n, (-1 / (1 - n))))), ((n - 4) * (1 - n) / 3))
    tao = tao_0 * (pow(fai, (1 / (n - 4))))
    if tao > 1:
        n = 1 + (1.285 * (math.log((H60P / H360P), 10)))
        tao_0 = (pow(0.278, k)) / (pow((m * pow(J, 1 / 3) / L), 4 / (4 - n)) * pow((S * F), (1 / (4 - n))))
        tao_c = pow(((1 - n) * S / miu), (1 / n))
        fai = pow(((tao_0 / tao_c) * (pow(n, (-1 / (1 - n))))), ((n - 4) * (1 - n) / 3))
        tao = tao_0 * (pow(fai, (1 / (n - 4))))
    else:
        n = 1 + (1.285 * (math.log((H10P / H60P), 10)))
    if tao > tao_c:
        Q = 0.278 * fai * (S / (pow(tao, n))) * F
    else:
        fai = 1 - ((miu / S) * (pow(tao_0, n)))
        Q = 0.278 * fai * (S / (pow(tao, n))) * F
    Zen = ((Dens-1)/(2.65-Dens))+1
    Qn = Q*Du*Zen
    Mw = ((19*Qn*1800)/72)/10000
    Ms = ((Dens-1)/1.65)*Mw
    Q_sum.append(Q)
    T_sum.append(tao)
    Qn_sum.append(Qn)
    Mw_sum.append(Mw)
    Ms_sum.append(Ms)
    time_sum.append(time)
Q_sum
T_sum
Qn_sum
Mw_sum
Ms_sum
time_sum

dataframe = pd.DataFrame({'Discharge': Q_sum, 'Time': T_sum, 'Qn': Qn_sum, 'Mw': Mw_sum, 'Ms': Ms_sum})
dataframe.to_csv('壳壳1210GPM01.csv', index=False, sep=',')
# from matplotlib import pyplot
# import matplotlib.pyplot as plt
# plt.rc('font',family='Arial')  #定义字体
# plt.figure(figsize=(7,5.5))    #设置图片大小
# font1 = {'family':'Arial','weight' : 'normal','size': 16,}
# plt.xticks(fontsize=14)       #设置坐标轴刻度字号
# plt.yticks(fontsize=14)
# plt.plot(time_sum,Q_sum)
# #设置横坐标说明
# plt.xlabel('Time (h)')
# #设置纵坐标说明
# plt.ylabel('Discharge (m/s)')
# #添加标题
# plt.title('T-Q')
# #设置纵坐标刻度
# my_x_ticks = np.arange(0, 60, 1)#原始数据有13个点，故此处为设置从0开始，间隔为1
# plt.xticks(my_x_ticks)
# #显示图表
# plt.show()
# plt.savefig(r"E:\data\keke\save_test.png",dpi=520)
