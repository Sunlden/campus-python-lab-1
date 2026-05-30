"""
第一章 数据自动化清洗 — DataFrame 创建与结构示例
对应章节 1.1 初识Pandas
运行方式: python dataframe_demo.py
"""

import pandas as pd

# ========== 1. 从多个 Series 构建 DataFrame ==========
print("=" * 50)
print("1. 从多个 Series 构建 DataFrame")
print("=" * 50)
s1 = pd.Series([85, 90, 78, 92, 88])
s2 = pd.Series(['男', '女', '男', '男', '女'])
s3 = pd.Series([16, 17, 16, 17, 16], index=[0, 1, 4, 2, 3])

df = pd.DataFrame({'成绩': s1, '性别': s2, '年龄': s3})
print(df)
print()

# ========== 2. 从字典列表创建 DataFrame ==========
print("=" * 50)
print("2. 从字典列表创建 DataFrame")
print("=" * 50)
students = [
    {'姓名': '张三', '班级': '高一(1)班', '项目': '100米', '手机号': '13800001111'},
    {'姓名': '李四', '班级': '高一(2)班', '项目': '跳远',   '手机号': '13900002222'},
    {'姓名': '王五', '班级': '高一(1)班', '项目': '铅球',   '手机号': '13700003333'},
    {'姓名': '赵六', '班级': '高一(3)班', '项目': '100米',  '手机号': '13600004444'},
]
df2 = pd.DataFrame(students)
print(df2)
print()

# ========== 3. 查看 DataFrame 结构信息 ==========
print("=" * 50)
print("3. 用 info() 查看结构")
print("=" * 50)
df2.info()
print()

# ========== 4. 基本属性查看 ==========
print("=" * 50)
print("4. DataFrame 基本属性")
print("=" * 50)
print(f"行数: {len(df2)}")
print(f"列名: {df2.columns.tolist()}")
print(f"数据类型:\n{df2.dtypes}")
print(f"\n前3行预览:\n{df2.head(3)}")
print(f"\n描述性统计:\n{df2.describe(include='all')}")
