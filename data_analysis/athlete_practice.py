"""
第一章 数据自动化清洗 — 实践活动：运动员体征数据清洗
对应章节 1.2 实践活动
运行方式: python athlete_practice.py

说明:
  本脚本模拟运动会长跑决赛中两套体征监测设备的数据清洗任务。
  设备A (智能腕表) — 心率 BPM
  设备B (智能跑鞋芯片) — 步频 SPM
  目标: 对齐时间、提取整分时刻、用前后均值填补缺失值
"""

import pandas as pd
import numpy as np

# ==========================================
# 步骤 1: 构建模拟体征数据
# ==========================================
print("=" * 60)
print("步骤 1: 构建模拟体征数据")
print("=" * 60)

# 心率数据 (模拟设备A — 有漏记)
hr_data = {
    '时间': [
        '08:00:15', '08:00:42', '08:01:10', '08:01:35',
        '08:02:05', '08:02:32', '08:03:08', '08:03:45',
        '08:04:12', '08:04:38'
    ],
    '心率_BPM': [142, 148, np.nan, 155, 160, np.nan, 168, 172, 175, 180]
}
df_hr = pd.DataFrame(hr_data)
print("心率表 (watch_hr):")
print(df_hr)

# 步频数据 (模拟设备B — 有漏记，时间有错位)
spm_data = {
    '时间': [
        '08:00:20', '08:00:48', '08:01:25', '08:02:08',
        '08:02:55', '08:03:15', '08:03:52', '08:04:22',
        '08:04:50', '08:05:05'
    ],
    '步频_SPM': [175, 178, 180, np.nan, 182, 185, np.nan, 188, 190, 192]
}
df_spm = pd.DataFrame(spm_data)
print("\n步频表 (shoes_spm):")
print(df_spm)

# ==========================================
# 步骤 2: 数据导入与预处理
# ==========================================
print("\n" + "=" * 60)
print("步骤 2: 转换时间格式")
print("=" * 60)

df_hr['时间'] = pd.to_datetime(df_hr['时间'], format='%H:%M:%S')
df_spm['时间'] = pd.to_datetime(df_spm['时间'], format='%H:%M:%S')
print("时间列已转换为 datetime 类型")

# ==========================================
# 步骤 3: 对齐合并 — merge()
# ==========================================
print("\n" + "=" * 60)
print("步骤 3: 以时间为基准合并两表")
print("=" * 60)

df_merged = pd.merge(df_hr, df_spm, on='时间', how='outer')
df_merged = df_merged.sort_values('时间').reset_index(drop=True)
print("合并后的数据 (含 NaN 占位):")
print(df_merged)

# ==========================================
# 步骤 4: 提取整分时刻
# ==========================================
print("\n" + "=" * 60)
print("步骤 4: 提取整分时刻")
print("=" * 60)

# 选取秒数为 0 的时间点
minute_mask = df_merged['时间'].dt.second == 0
df_minute = df_merged[minute_mask].copy()
print("整分时刻数据:")
print(df_minute)

# 如果整分时刻数据不足，手动构造整分序列
time_range = pd.date_range(
    start=df_merged['时间'].min().floor('min'),
    end=df_merged['时间'].max().floor('min'),
    freq='min'
)
df_minute_index = pd.DataFrame({'时间': time_range})
print(f"\n完整整分时刻序列 ({len(df_minute_index)} 个时间点):")
print(df_minute_index)

# ==========================================
# 步骤 5: 均值填补缺失值
# ==========================================
print("\n" + "=" * 60)
print("步骤 5: 用前后相邻值的均值填补缺失")
print("=" * 60)

# 对所有列做向前和向后插值，然后取平均
df_merged.set_index('时间', inplace=True)

# 对每个整分时刻: 取前后最近有效值的平均
for col in ['心率_BPM', '步频_SPM']:
    # 线性插值
    df_merged[col] = df_merged[col].interpolate(method='linear')

df_merged.reset_index(inplace=True)
print("插值填补后的完整数据:")
print(df_merged)

# ==========================================
# 步骤 6: 提取最终整分报告
# ==========================================
print("\n" + "=" * 60)
print("步骤 6: 教练组所需的最终整分时刻报告")
print("=" * 60)

# 将合并数据按整分时刻筛选
df_merged['整分时刻'] = df_merged['时间'].dt.floor('min')
# 对每个整分时刻取平均值
df_final = df_merged.groupby('整分时刻').agg({
    '心率_BPM': 'mean',
    '步频_SPM': 'mean'
}).round(1).reset_index()

df_final['整分时刻'] = df_final['整分时刻'].dt.strftime('%H:%M:%S')
print(df_final)
print("\n清洗完成! 报告已生成。")
