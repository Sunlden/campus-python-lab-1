"""
第二章 数据可视化与信息传递 — Pandas 快速绘图示例
对应章节 2.2.6 利用 Pandas 快速绘图
运行方式: python pandas_quick_plot.py
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
# 构建示例数据
# ==========================================
np.random.seed(42)
data = {
    '班级': np.random.choice(['高一(1)班', '高一(2)班', '高一(3)班', '高一(4)班'], 200),
    '项目': np.random.choice(['100米', '200米', '400米', '800米', '跳远', '跳高', '铅球'], 200),
    '性别': np.random.choice(['男', '女'], 200, p=[0.55, 0.45]),
}
df = pd.DataFrame(data)

print("原始数据预览:")
print(df.head(10))
print(f"\n总记录数: {len(df)}")

# ==========================================
# 1. Pandas 快速绘制柱状图
# ==========================================
print("\n[1] Pandas 快速柱状图...")
proj_count = df['项目'].value_counts()
proj_count.plot(kind='bar', figsize=(8, 5), color='steelblue',
                edgecolor='white', title='各项目报名人数 (Pandas快速绘图)')
plt.xlabel('比赛项目')
plt.ylabel('报名人数')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('pandas_bar.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → pandas_bar.png 已保存")

# ==========================================
# 2. Pandas 快速绘制折线图
# ==========================================
print("[2] Pandas 快速折线图...")

# 构造时间序列
days = pd.date_range('2025-03-10', periods=7, freq='D')
lib_data = pd.Series([128, 145, 132, 156, 182, 175, 195], index=days)
lib_data.plot(kind='line', figsize=(8, 5), marker='o',
              color='coral', linewidth=2, title='图书馆借阅人数变化趋势 (Pandas快速绘图)')
plt.xlabel('日期')
plt.ylabel('借阅人数')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('pandas_line.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → pandas_line.png 已保存")

# ==========================================
# 3. Pandas 快速绘制饼图
# ==========================================
print("[3] Pandas 快速饼图...")
gender_count = df['性别'].value_counts()
gender_count.plot(kind='pie', figsize=(7, 7), autopct='%1.1f%%',
                  startangle=90, colors=['#6baed6', '#fdae6b'],
                  title='报名学生男女比例 (Pandas快速绘图)')
plt.ylabel('')
plt.tight_layout()
plt.savefig('pandas_pie.png', dpi=150, bbox_inches='tight')
plt.close()
print("  → pandas_pie.png 已保存")

# ==========================================
# 对比总结
# ==========================================
print("""
    Pandas 快速绘图 vs Matplotlib 直接绘制:

    Pandas 优势:
    - 代码更简洁，一行即可生成图表
    - 自动使用 DataFrame 的索引和列名作为标签
    - 适合快速探索数据

    Matplotlib 优势:
    - 对图表元素的控制更精细
    - 适合需要复杂布局的场景
    - 可进行高度定制化的美化

    建议: 探索阶段用 Pandas 快速出图，正式报告用 Matplotlib 精调。
    """)
