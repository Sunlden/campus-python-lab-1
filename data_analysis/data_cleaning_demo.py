"""
第一章 数据自动化清洗 — 数据清洗核心操作示例
对应章节 1.2 数据的导入与初步审查
运行方式: python data_cleaning_demo.py
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("数据清洗核心操作演示")
print("=" * 60)

# ========== 构建模拟脏数据 ==========
data = {
    '姓名':    ['张三', '李四', '王五', '赵六', '陈七', '张三'],
    '班级':    ['高一(1)', '高一(2)', None, '高一(3)', '高一(1)', '高一(1)'],
    '项目':    ['100米', '跳远', '铅球', '100米', None, '100米'],
    '手机号':  ['13800001111', '1390000', '13700003333', None, '13500005555', '13800001111'],
    '年龄':    [16, 17, 16, -5, 17, 16],
}
df = pd.DataFrame(data)
print("\n原始数据 (含脏数据):")
print(df)
print()

# ========== 1. 检查缺失值 ==========
print("=" * 60)
print("1. 检查缺失值 — isnull()")
print("=" * 60)
print(df.isnull())
print(f"\n各列缺失值数量:\n{df.isnull().sum()}")

# ========== 2. 填充缺失值 ==========
print("\n" + "=" * 60)
print("2. 填充缺失值 — fillna()")
print("=" * 60)
df_filled = df.copy()
df_filled['班级'] = df_filled['班级'].fillna('暂无')
df_filled['项目'] = df_filled['项目'].fillna('待确认')
df_filled['手机号'] = df_filled['手机号'].fillna('未填写')
print(df_filled)

# ========== 3. 过滤缺失行 ==========
print("\n" + "=" * 60)
print("3. 过滤含缺失值的行 — dropna()")
print("=" * 60)
df_dropped = df.dropna()
print(f"删除含 NaN 的行后 (剩余 {len(df_dropped)} 行):")
print(df_dropped)

# ========== 4. 检测和过滤异常值 ==========
print("\n" + "=" * 60)
print("4. 过滤异常值 — query()")
print("=" * 60)
df_valid_age = df_filled.query('年龄 > 0 and 年龄 < 120')
print(f"过滤异常年龄后 (剩余 {len(df_valid_age)} 行):")
print(df_valid_age)

# ========== 5. 移除重复数据 ==========
print("\n" + "=" * 60)
print("5. 移除重复行 — drop_duplicates()")
print("=" * 60)
df_unique = df_valid_age.drop_duplicates()
print(f"去重后 (剩余 {len(df_unique)} 行):")
print(df_unique)

# ========== 6. 最终清洗结果对比 ==========
print("\n" + "=" * 60)
print("6. 清洗前后对比")
print("=" * 60)
print(f"原始数据行数: {len(df)}")
print(f"清洗后行数:   {len(df_unique)}")
print(f"移除行数:     {len(df) - len(df_unique)}")
print("\n清洗后的干净数据:")
print(df_unique)
