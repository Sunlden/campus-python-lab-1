"""
第二章 数据可视化与信息传递 — 基础图表绘制
对应章节 2.2 利用 Python 绘制基础图表
运行方式: python basic_plotting.py
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==========================================
# 设置中文字体 (Windows: SimHei / macOS: PingFang SC)
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示异常

# ==========================================
# 1. 柱状图：比较不同类别的数量
# ==========================================
print("绘制柱状图...")

projects = ['100米', '200米', '400米', '800米', '跳远', '跳高', '铅球']
counts = [45, 32, 38, 28, 25, 15, 22]

plt.figure(figsize=(8, 5))
plt.bar(projects, counts, color='steelblue', edgecolor='white', linewidth=0.8)
plt.title('各比赛项目报名人数统计', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('比赛项目', fontsize=12)
plt.ylabel('报名人数', fontsize=12)
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('bar_project_count.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → bar_project_count.png 已保存")

# ==========================================
# 2. 折线图：观察数据变化趋势
# ==========================================
print("绘制折线图...")

time = ['08:00', '08:05', '08:10', '08:15', '08:20', '08:25', '08:30']
heart_rate = [72, 140, 158, 162, 168, 175, 180]

plt.figure(figsize=(8, 5))
plt.plot(time, heart_rate, marker='o', color='coral',
         linewidth=2, markersize=8, markerfacecolor='white',
         markeredgewidth=2, markeredgecolor='coral')
plt.title('运动员比赛过程中心率变化趋势', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('时间', fontsize=12)
plt.ylabel('心率 (BPM)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('line_heart_rate.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → line_heart_rate.png 已保存")

# ==========================================
# 3. 饼图：展示整体中的比例
# ==========================================
print("绘制饼图...")

genders = ['男生', '女生']
gender_counts = [135, 87]
colors_pie = ['#6baed6', '#fdae6b']
explode = (0.02, 0)

plt.figure(figsize=(7, 7))
plt.pie(gender_counts, labels=genders, colors=colors_pie,
        autopct='%1.1f%%', startangle=90, explode=explode,
        textprops={'fontsize': 13}, pctdistance=0.6)
plt.title('报名学生男女比例', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('pie_gender_ratio.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → pie_gender_ratio.png 已保存")

# ==========================================
# 4. 散点图：观察两个变量之间的关系
# ==========================================
print("绘制散点图...")

np.random.seed(42)
heights = np.random.normal(170, 8, 60)
jump_scores = heights * 1.2 + np.random.normal(0, 10, 60)

plt.figure(figsize=(8, 5))
plt.scatter(heights, jump_scores, c='steelblue', alpha=0.6,
            edgecolors='white', linewidth=0.5, s=60)
plt.title('学生身高与跳远成绩关系', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('身高 (cm)', fontsize=12)
plt.ylabel('跳远成绩 (cm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('scatter_height_jump.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → scatter_height_jump.png 已保存")

print("\n所有基础图表已生成完毕。")
