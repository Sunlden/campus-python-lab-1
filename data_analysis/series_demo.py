"""
第一章 数据自动化清洗 — Series 创建与操作示例
对应章节 1.1 初识Pandas
运行方式: python series_demo.py
"""

import pandas as pd

# ========== 1. 默认整数索引创建 Series ==========
print("=" * 50)
print("1. 默认整数索引创建 Series")
print("=" * 50)
scores = pd.Series([98, 87, 92, 76, 85])
print(scores)
print()

# ========== 2. 自定义索引创建 Series ==========
print("=" * 50)
print("2. 以学生姓名作为标签索引")
print("=" * 50)
scores_named = pd.Series(
    [98, 87, 92, 76, 85],
    index=['张三', '李四', '王五', '赵六', '陈七']
)
print(scores_named)
print()

# ========== 3. 通过标签快速访问 ==========
print("=" * 50)
print("3. 通过标签访问特定数据")
print("=" * 50)
print(f"张三的成绩: {scores_named['张三']}")
print(f"王五的成绩: {scores_named['王五']}")
print()

# ========== 4. 查看 Series 的索引和值 ==========
print("=" * 50)
print("4. 查看索引和值")
print("=" * 50)
print(f"索引 (index): {scores_named.index.tolist()}")
print(f"值 (values): {scores_named.values}")
print()

# ========== 5. 缺失数据标识 NaN ==========
print("=" * 50)
print("5. 缺失数据自动标识为 NaN")
print("=" * 50)
import numpy as np
data_with_nan = pd.Series([10, np.nan, 30, None, 50])
print(data_with_nan)
print(f"检测缺失值:\n{data_with_nan.isnull()}")
print()

# ========== 6. 自动对齐特性 ==========
print("=" * 50)
print("6. Series 自动对齐运算")
print("=" * 50)
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
print(f"s1:\n{s1}")
print(f"\ns2:\n{s2}")
print(f"\ns1 + s2 (自动对齐后):\n{s1 + s2}")
print("注意: 'a'和'd'只在一边存在, 结果为 NaN")
