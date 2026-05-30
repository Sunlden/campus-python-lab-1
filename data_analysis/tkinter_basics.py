"""
第三章 打造"校园管家" — tkinter 基础组件与布局
对应章节 3.1 认识图形界面——tkinter入门
运行方式: python tkinter_basics.py
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox

# ==========================================
# 示例 1: 第一个 GUI 窗口
# ==========================================
def demo_first_window():
    """创建一个简单的空白窗口"""
    root = tk.Tk()
    root.title("校园管家 v1.0")
    root.geometry("400x300")
    root.mainloop()


# ==========================================
# 示例 2: 带标签和按钮的窗口
# ==========================================
def demo_label_button():
    root = tk.Tk()
    root.title("组件演示")
    root.geometry("350x250")

    # 标签
    label = tk.Label(root, text="欢迎使用校园管家!",
                     font=("黑体", 14), fg="#2c2416")
    label.pack(pady=20)

    # 按钮
    def on_click():
        label.config(text="你点击了按钮!")

    btn = tk.Button(root, text="点击我", command=on_click,
                    width=15, bg="#90EE90", font=("微软雅黑", 11))
    btn.pack(pady=10)

    root.mainloop()


# ==========================================
# 示例 3: 完整界面 — 带标签/按钮/文本框/Frame
# ==========================================
def demo_full_interface():
    """搭建'校园管家'主界面"""
    root = tk.Tk()
    root.title("校园管家 - 校运会数据分析助手")
    root.geometry("650x500")

    # --- 标题标签 ---
    title_label = tk.Label(root, text="校园运动会数据智能分析平台",
                           font=("黑体", 16), fg="#2c2416")
    title_label.pack(pady=10)

    # --- 文件选择区域 (Frame) ---
    file_frame = tk.Frame(root)
    file_frame.pack(pady=10)

    path_label = tk.Label(file_frame, text="未选择任何文件",
                          fg="gray", width=40, bg="white", relief="sunken")
    path_label.pack(side=tk.LEFT, padx=5)

    select_btn = tk.Button(file_frame, text="选择文件", width=10)
    select_btn.pack(side=tk.LEFT)

    # --- 功能按钮区域 ---
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=20)

    clean_btn = tk.Button(btn_frame, text="一键数据清洗", width=15,
                          bg="#90EE90", font=("微软雅黑", 10))
    clean_btn.pack(side=tk.LEFT, padx=10)

    plot_btn = tk.Button(btn_frame, text="生成可视化图表", width=15,
                         bg="#87CEEB", font=("微软雅黑", 10))
    plot_btn.pack(side=tk.LEFT, padx=10)

    # --- 结果显示区域 (带滚动条) ---
    result_text = scrolledtext.ScrolledText(
        root, height=15, width=70, font=("微软雅黑", 10)
    )
    result_text.pack(pady=10)
    result_text.insert(tk.END, "【系统日志】欢迎使用校园管家！\n")
    result_text.insert(tk.END, "请点击\"选择文件\"按钮导入数据。\n")

    root.mainloop()


# ==========================================
# 示例 4: 对话框使用
# ==========================================
def demo_dialogs():
    root = tk.Tk()
    root.title("对话框演示")
    root.geometry("300x200")

    def show_info():
        messagebox.showinfo("提示", "这是一条信息提示!")

    def show_warning():
        messagebox.showwarning("警告", "请先选择数据文件!")

    def show_error():
        messagebox.showerror("错误", "处理失败!")

    def ask_yes_no():
        result = messagebox.askyesno("确认", "确定要退出吗?")
        if result:
            root.destroy()

    tk.Button(root, text="信息提示", command=show_info, width=15).pack(pady=5)
    tk.Button(root, text="警告提示", command=show_warning, width=15).pack(pady=5)
    tk.Button(root, text="错误提示", command=show_error, width=15).pack(pady=5)
    tk.Button(root, text="确认退出", command=ask_yes_no, width=15).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    print("tkinter 基础演示")
    print("1 - 运行第一个空窗口")
    print("2 - 运行标签+按钮演示")
    print("3 - 运行完整界面演示")
    print("4 - 运行对话框演示")
    choice = input("请选择 (1/2/3/4): ").strip()

    if choice == "1":
        demo_first_window()
    elif choice == "2":
        demo_label_button()
    elif choice == "3":
        demo_full_interface()
    elif choice == "4":
        demo_dialogs()
    else:
        print("无效选择")
