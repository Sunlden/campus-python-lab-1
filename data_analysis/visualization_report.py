"""
第二章 数据可视化与信息传递 — 校园运动会报名数据可视化完整报告
对应章节 项目实施: "让校园数据开口说话"
运行方式: python visualization_report.py
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
# 构建清洗后的模拟报名数据
# ==========================================
np.random.seed(42)

classes = ['高一(1)班', '高一(2)班', '高一(3)班', '高一(4)班', '高一(5)班']
projects = ['100米', '200米', '400米', '800米', '跳远', '跳高', '铅球']

students = []
for i in range(222):
    cls = np.random.choice(classes)
    gender = np.random.choice(['男', '女'], p=[0.55, 0.45])
    proj = np.random.choice(projects)
    students.append({'班级': cls, '性别': gender, '项目': proj})

df = pd.DataFrame(students)
print(f"共 {len(df)} 条报名记录")
print(df.head(8))

# ==========================================
# 图 1: 各项目报名人数柱状图
# ==========================================
print("\n[1/5] 绘制各项目报名人数柱状图...")

proj_count = df['项目'].value_counts()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(proj_count.index, proj_count.values,
              color='steelblue', edgecolor='white', linewidth=0.8)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=11)

ax.set_title('各比赛项目报名人数统计', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('比赛项目', fontsize=12)
ax.set_ylabel('报名人数', fontsize=12)
ax.set_xticklabels(proj_count.index, rotation=30)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('report_fig1_projects.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → report_fig1_projects.png 已保存")

# ==========================================
# 图 2: 各班报名人数柱状图
# ==========================================
print("[2/5] 绘制各班报名人数柱状图...")

class_count = df['班级'].value_counts()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(class_count.index, class_count.values,
              color='#6baed6', edgecolor='white', linewidth=0.8)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=11)

ax.set_title('各班报名人数统计', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('班级', fontsize=12)
ax.set_ylabel('报名人数', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('report_fig2_classes.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → report_fig2_classes.png 已保存")

# ==========================================
# 图 3: 男女生报名比例饼图
# ==========================================
print("[3/5] 绘制男女生报名比例饼图...")

gender_count = df['性别'].value_counts()

fig, ax = plt.subplots(figsize=(7, 7))
colors_pie = ['#6baed6', '#fdae6b']
explode = (0.02, 0)

wedges, texts, autotexts = ax.pie(
    gender_count.values, labels=gender_count.index, colors=colors_pie,
    autopct='%1.1f%%', startangle=90, explode=explode,
    textprops={'fontsize': 13}, pctdistance=0.6
)
for at in autotexts:
    at.set_fontweight('bold')

ax.set_title('报名学生男女比例', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('report_fig3_gender.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → report_fig3_gender.png 已保存")

# ==========================================
# 图 4: 各班男女分组柱状图
# ==========================================
print("[4/5] 绘制各班男女分组柱状图...")

cross_tab = pd.crosstab(df['班级'], df['性别'])

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(classes))
width = 0.33

bars_m = ax.bar(x - width/2, cross_tab['男'], width, label='男生',
                color='#6baed6', edgecolor='white')
bars_f = ax.bar(x + width/2, cross_tab['女'], width, label='女生',
                color='#fdae6b', edgecolor='white')

for bar in bars_m:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            str(int(bar.get_height())), ha='center', fontsize=9)
for bar in bars_f:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            str(int(bar.get_height())), ha='center', fontsize=9)

ax.set_title('各班男女生报名人数对比', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('班级', fontsize=12)
ax.set_ylabel('报名人数', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(classes)
ax.legend(fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('report_fig4_class_gender.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → report_fig4_class_gender.png 已保存")

# ==========================================
# 图 5: 自选 — 热力图：班级×项目交叉分析
# ==========================================
print("[5/5] 绘制班级×项目热力图...")

cross_tab2 = pd.crosstab(df['班级'], df['项目'])

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(cross_tab2.values, cmap='YlOrRd', aspect='auto')

ax.set_xticks(np.arange(len(projects)))
ax.set_yticks(np.arange(len(classes)))
ax.set_xticklabels(projects, rotation=30)
ax.set_yticklabels(classes)

# 在格子中标注数值
for i in range(len(classes)):
    for j in range(len(projects)):
        val = cross_tab2.values[i, j]
        ax.text(j, i, str(val), ha='center', va='center',
                fontsize=10, fontweight='bold',
                color='white' if val > cross_tab2.values.max() / 2 else 'black')

cbar = plt.colorbar(im, ax=ax)
cbar.set_label('报名人数', fontsize=11)

ax.set_title('各班各项目报名人数热力图', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('比赛项目', fontsize=12)
ax.set_ylabel('班级', fontsize=12)
plt.tight_layout()
plt.savefig('report_fig5_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("  → report_fig5_heatmap.png 已保存")

print("\n" + "=" * 50)
print("可视化报告生成完毕! 共 5 张图表。")
print("=" * 50)
print("""
分析结论:
1. 从图1可以看出，各项目报名人数分布较为均匀。
2. 从图2可以看出，各班报名人数存在一定差异。
3. 从图3可以看出，男女参与比例大体接近校内实际比例。
4. 从图4可以看出，各班男女参与情况各有特点。
5. 从图5的热力图可以一目了然地看出各班级在不同项目上的参与热度。
""")
