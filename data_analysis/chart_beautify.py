"""
第二章 数据可视化与信息传递 — 图表美化完整示例
对应章节 2.3 图表美化与信息表达
运行方式: python chart_beautify.py
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==========================================
# 设置中文字体
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 示例 1: 分组柱状图 — 各班男女报名人数对比
# ==========================================
print("绘制分组柱状图...")

classes = ['高一(1)班', '高一(2)班', '高一(3)班', '高一(4)班']
boys = [18, 22, 15, 20]
girls = [14, 12, 18, 13]

x = np.arange(len(classes))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))
bars1 = ax.bar(x - width/2, boys, width, label='男生',
               color='#6baed6', edgecolor='white', linewidth=0.8)
bars2 = ax.bar(x + width/2, girls, width, label='女生',
               color='#fdae6b', edgecolor='white', linewidth=0.8)

# 添加数据标注
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=10)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=10)

ax.set_title('各班男女生报名人数对比', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('班级', fontsize=12)
ax.set_ylabel('报名人数', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(classes)
ax.legend(loc='upper right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.set_ylim(0, max(boys + girls) + 5)
plt.tight_layout()
plt.savefig('bar_class_gender.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → bar_class_gender.png 已保存 (含数据标注)")

# ==========================================
# 示例 2: 突出某个类别的柱状图
# ==========================================
print("绘制重点突出柱状图...")

projects = ['100米', '200米', '400米', '800米', '跳远', '跳高', '铅球']
counts = [45, 32, 38, 28, 25, 15, 22]
colors_bar = ['orange' if p == '100米' else 'steelblue' for p in projects]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(projects, counts, color=colors_bar, edgecolor='white', linewidth=0.8)

# 只为重点柱子添加标注
for bar, proj in zip(bars, projects):
    if proj == '100米':
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
                f'最热: {int(bar.get_height())}人', ha='center', va='bottom',
                fontsize=11, fontweight='bold', color='darkorange')

ax.set_title('各项目报名人数 (100米最受欢迎)', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('比赛项目', fontsize=12)
ax.set_ylabel('报名人数', fontsize=12)
ax.set_xticklabels(projects, rotation=30)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('bar_highlight.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → bar_highlight.png 已保存 (重点突出)")

# ==========================================
# 示例 3: 带网格的折线图
# ==========================================
print("绘制带网格折线图...")

days = ['周一', '周二', '周三', '周四', '周五']
borrow = [128, 145, 132, 156, 182]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(days, borrow, marker='D', color='#2c7fb8', linewidth=2.5,
        markersize=10, markerfacecolor='white', markeredgewidth=2,
        markeredgecolor='#2c7fb8')
ax.set_title('一周内图书馆每日借阅人数变化', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('日期', fontsize=12)
ax.set_ylabel('借阅人数', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

# 标注每个数据点
for d, b in zip(days, borrow):
    ax.annotate(f'{b}人', (d, b), textcoords='offset points',
                xytext=(0, 12), ha='center', fontsize=10, color='#2c7fb8')

plt.tight_layout()
plt.savefig('line_library.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → line_library.png 已保存 (含数据标注+网格)")

# ==========================================
# 示例 4: 保存图表的完整流程
# ==========================================
print("演示完整保存流程...")

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(['A组', 'B组', 'C组'], [85, 92, 78],
       color=['#a1dab4', '#41b6c4', '#2c7fb8'], edgecolor='white')
ax.set_title('各组平均分对比', fontsize=15, fontweight='bold')
ax.set_ylabel('平均分')
ax.grid(axis='y', linestyle='--', alpha=0.3)

# savefig 应在 show() 之前调用
plt.savefig('final_report.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("  → final_report.png 已保存 (高分辨率 300dpi)")

print("\n所有美化图表已生成完毕。")
