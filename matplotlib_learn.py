# encoding: utf-8
"""
@author: lin
@file: matplotlib_learn.py.py
@time: 2018/10/13 0:08
@desc:"利用Python进行数据分析".pdf matplotlib 学习
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
from datetime import datetime

'''Figure 和 subplot'''
fig1 = plt.figure()
# 不能通过空Figure绘图。必须用add_subplot创建
# 图像2x2 ,且选中第一个subplot
ax1 = fig1.add_subplot(2, 2, 1)
ax2 = fig1.add_subplot(2, 2, 2)
ax3 = fig1.add_subplot(2, 2, 3)

# plt.plot 在最后一个用过的subplot绘制，
# 'k--'是一个线型选项，绘制黑色虚线图
plt.plot(randn(50).cumsum(), 'k--')
# 柱状图
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
# 散点图
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

# plt.subplots 创建新的figure和
# 返回一个含有已创建的subplot对象的numpy数组
fig2, axes = plt.subplots(2, 3)
print(axes)
# 调整subplot周围的间距,plt.subplots_adjust,wspace和hspace控制百分比
fig3, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0.2, hspace=0.2)

'''颜色、标记和线型'''
fig4, ax = plt.subplots(1, 1)

data1 = randn(30).cumsum()
data2 = randn(30).cumsum()
# 非实际数据点默认按线性方式插值
# 颜色，实际数据标记，线型
ax.plot(data1, 'go--', label='Default')
# drawstyle 改变插值方式
ax.plot(data2, 'k*-', drawstyle='steps-post', label='steps-post')

'''刻度、标签和图例'''
# (1)设置标题、轴标签、刻度以及刻度标签
fig5 = plt.figure()
ax1 = fig5.add_subplot(1, 2, 1)
ax2 = fig5.add_subplot(1, 2, 2)
ax1.plot(randn(1000).cumsum())
ax2.plot(randn(1000).cumsum())
ax2.set_xlim([0, 1000])
# 告诉maplotlb要将刻度放在数据范围的哪些位置
# 默认情况下， 这些位置也就是刻度标签
ticks = ax2.set_xticks([0, 200, 400, 600, 800])
# 将任何其他的值用做标签
labels = ax2.set_xticklabels(['one', 'two', 'three', 'four',
                              'five'], rotation=30, fontsize='small')
# set_xlabel为x轴取名，set_title取标题
ax2.set_title("my first matplotlib plot")
ax2.set_xlabel("Stages")
# (2)添加图例
# 添加标签
fig6, ax = plt.subplots(1, 1)
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
# 创建图例 loc='best'自适应位置
ax.legend(loc='best')

'''注解以及在Subplot上绘图'''
# 注解可以通过text、arrow、annotate等函数添加
fig7, ax = plt.subplots(1, 1)
# text将文本绘制在图表到的指定坐标（x,y）
# x = [1, 2, 3]
# y = [1, 2, 3]
# ax.text(x, y, 'hello world!', family='monospace', fontsize=10)

# 2008-2009年金融危机示例未打

# 图形的绘制
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

plt.show()