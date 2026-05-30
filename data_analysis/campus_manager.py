"""
第三章 打造"校园管家" — 完整应用软件
整合第一章 Pandas 数据清洗 + 第二章 Matplotlib 可视化
运行方式: python campus_manager.py
打包命令: pyinstaller -F -w campus_manager.py
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# 全局设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'PingFang SC']
plt.rcParams['axes.unicode_minus'] = False

SAVE_DIR = os.path.join(os.path.expanduser("~"), "校园管家输出")
CLEANED_FILE = os.path.join(SAVE_DIR, "报名表_清洗后_GUI版.xlsx")
BAR_CHART = os.path.join(SAVE_DIR, "各项目报名人数.png")
PIE_CHART = os.path.join(SAVE_DIR, "男女生比例.png")


# ==========================================
# 主线窗口布局
# ==========================================
def create_main_window():
    """创建主窗口并布局所有控件"""
    root = tk.Tk()
    root.title("校运会报名数据处理工具 — 校园管家 v2.0")
    root.geometry("700x600")
    root.configure(bg='#fdf8f0')

    # --- 标题 ---
    title_label = tk.Label(
        root, text="校园运动会数据智能分析平台",
        font=("黑体", 18), fg="#2c2416", bg='#fdf8f0'
    )
    title_label.pack(pady=12)

    # --- 文件选择区域 ---
    frame_file = tk.Frame(root, bg='#fdf8f0')
    frame_file.pack(pady=8)

    tk.Label(frame_file, text="📂", font=("", 14), bg='#fdf8f0').pack(side=tk.LEFT)

    btn_select = tk.Button(
        frame_file, text="1. 选择报名表文件", width=20,
        font=("微软雅黑", 10), bg="#d4e6f1",
        activebackground="#aed6f1", cursor="hand2"
    )
    btn_select.pack(side=tk.LEFT, padx=5)

    lbl_path = tk.Label(
        frame_file, text="未选择任何文件", fg="gray",
        width=42, anchor="w", bg="white", relief="sunken"
    )
    lbl_path.pack(side=tk.LEFT, padx=5)

    # --- 功能按钮区域 ---
    frame_buttons = tk.Frame(root, bg='#fdf8f0')
    frame_buttons.pack(pady=12)

    btn_clean = tk.Button(
        frame_buttons, text="2. 一键数据清洗", width=20,
        font=("微软雅黑", 10), bg="#a9dfbf",
        activebackground="#7dcea0", cursor="hand2"
    )
    btn_clean.pack(side=tk.LEFT, padx=8)

    btn_plot = tk.Button(
        frame_buttons, text="3. 生成统计图表", width=20,
        font=("微软雅黑", 10), bg="#aed6f1",
        activebackground="#85c1e9", cursor="hand2"
    )
    btn_plot.pack(side=tk.LEFT, padx=8)

    # --- 日志显示区域 ---
    frame_log = tk.Frame(root, bg='#fdf8f0')
    frame_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tk.Label(
        frame_log, text="运行日志:", font=("微软雅黑", 9),
        fg="#6b5e4a", bg='#fdf8f0', anchor="w"
    ).pack(fill=tk.X)

    txt_result = scrolledtext.ScrolledText(
        frame_log, height=18, wrap=tk.WORD,
        font=("微软雅黑", 9), bg='#fffef9', fg='#2c2416'
    )
    txt_result.pack(fill=tk.BOTH, expand=True)
    txt_result.insert(tk.END, "【系统日志】欢迎使用校园管家 v2.0！\n")
    txt_result.insert(tk.END, "【系统日志】请点击\"选择文件\"按钮导入报名表，\n")
    txt_result.insert(tk.END, "【系统日志】然后依次点击\"数据清洗\"和\"生成图表\"。\n")
    txt_result.insert(tk.END, "-" * 55 + "\n")

    return root, lbl_path, txt_result, btn_select, btn_clean, btn_plot


# ==========================================
# 核心功能函数
# ==========================================
def select_file(path_label):
    """选择文件并更新路径标签"""
    filepath = filedialog.askopenfilename(
        title="选择校运会报名表",
        filetypes=[("Excel 文件", "*.xlsx"), ("所有文件", "*.*")]
    )
    if filepath:
        path_label.config(text=filepath, fg="black")


def run_data_cleaning(path_label, result_text):
    """数据清洗：去重 + 删除空报名项目，保存到 SAVE_DIR"""
    file_path = path_label.cget("text")

    if file_path == "未选择任何文件":
        messagebox.showwarning("警告", "请先选择数据文件！")
        return

    try:
        result_text.insert(tk.END, ">>> 开始执行数据清洗...\n")
        result_text.see(tk.END)
        root = path_label.winfo_toplevel()
        root.update()

        df = pd.read_excel(file_path)
        result_text.insert(tk.END, f">>> 成功读取文件，共 {len(df)} 条记录。\n")

        # 删除完全重复的行
        before_drop = len(df)
        df = df.drop_duplicates()
        result_text.insert(
            tk.END, f">>> 删除重复数据 {before_drop - len(df)} 条。\n"
        )

        # 删除"报名项目"列为空的行
        if '报名项目' in df.columns:
            before_drop_na = len(df)
            df = df.dropna(subset=['报名项目'])
            result_text.insert(
                tk.END, f">>> 删除\"报名项目\"为空的记录 {before_drop_na - len(df)} 条。\n"
            )
        else:
            result_text.insert(
                tk.END, "!!! 警告：表格中没有\"报名项目\"列，请检查列名。\n"
            )

        os.makedirs(SAVE_DIR, exist_ok=True)
        df.to_excel(CLEANED_FILE, index=False)
        result_text.insert(
            tk.END, f">>> 数据清洗完成！结果已保存为: {CLEANED_FILE}\n"
        )
        result_text.see(tk.END)
        messagebox.showinfo("完成",
                            f"数据清洗成功！\n清洗后文件：\n{CLEANED_FILE}")

    except Exception as e:
        result_text.insert(tk.END, f"!!! 清洗过程中发生错误: {str(e)}\n")
        messagebox.showerror("错误", f"处理失败：{str(e)}")


def generate_charts(path_label, result_text):
    """基于清洗后的文件生成柱状图和饼图"""
    if not os.path.exists(CLEANED_FILE):
        messagebox.showwarning(
            "警告",
            f"未找到清洗后的文件：\n{CLEANED_FILE}\n请先点击\"一键数据清洗\"！"
        )
        return

    try:
        result_text.insert(tk.END, ">>> 开始生成可视化图表...\n")
        result_text.see(tk.END)
        root = path_label.winfo_toplevel()
        root.update()

        df = pd.read_excel(CLEANED_FILE)
        result_text.insert(
            tk.END, f">>> 成功读取清洗后文件，共 {len(df)} 条记录。\n"
        )

        # 柱状图：各项目报名人数
        if '报名项目' in df.columns:
            project_count = df['报名项目'].value_counts()
            result_text.insert(
                tk.END, f">>> 报名项目统计：\n{project_count.to_string()}\n"
            )

            plt.figure(figsize=(8, 5))
            plt.bar(project_count.index, project_count.values,
                    color='steelblue', edgecolor='white')
            plt.title('各比赛项目报名人数统计', fontsize=14, fontweight='bold')
            plt.xlabel('比赛项目')
            plt.ylabel('报名人数')
            plt.xticks(rotation=30)
            plt.tight_layout()
            plt.savefig(BAR_CHART, dpi=300, bbox_inches='tight')
            plt.close()
            result_text.insert(
                tk.END, f">>> 柱状图已保存: {BAR_CHART}\n"
            )

        # 饼图：男女生比例
        if '性别' in df.columns:
            gender_count = df['性别'].value_counts()
            result_text.insert(
                tk.END, f">>> 性别统计：\n{gender_count.to_string()}\n"
            )

            plt.figure(figsize=(6, 6))
            plt.pie(gender_count.values, labels=gender_count.index,
                    autopct='%1.1f%%', startangle=90,
                    colors=['#6baed6', '#fdae6b'])
            plt.title('男女生报名比例', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.savefig(PIE_CHART, dpi=300, bbox_inches='tight')
            plt.close()
            result_text.insert(
                tk.END, f">>> 饼图已保存: {PIE_CHART}\n"
            )

        result_text.see(tk.END)
        messagebox.showinfo("完成",
                            f"图表已生成并保存到：\n{BAR_CHART}\n{PIE_CHART}")

    except Exception as e:
        result_text.insert(tk.END, f"!!! 生成图表时发生错误: {str(e)}\n")
        messagebox.showerror("错误", f"绘图失败：{str(e)}")


# ==========================================
# 程序入口
# ==========================================
if __name__ == "__main__":
    root, path_label, result_text, select_btn, clean_btn, plot_btn = \
        create_main_window()

    # 绑定回调函数
    select_btn.config(command=lambda: select_file(path_label))
    clean_btn.config(command=lambda: run_data_cleaning(path_label, result_text))
    plot_btn.config(command=lambda: generate_charts(path_label, result_text))

    root.mainloop()
