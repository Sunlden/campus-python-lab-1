"""
第三章 打造"校园管家" — 事件驱动编程与回调函数
对应章节 3.2 事件驱动——为按钮绑定功能
运行方式: python event_driven_demo.py
"""

import tkinter as tk

# ==========================================
# 示例 1: 基础回调函数
# ==========================================
def demo_basic_callback():
    """演示按钮点击 → 回调函数 → 更新标签"""

    def on_button_click():
        """回调函数：按钮被点击时执行"""
        print("按钮被点击了！")  # 控制台输出
        label.config(text="你好，校园管家！")  # 更新标签文字

    root = tk.Tk()
    root.title("回调函数示例")
    root.geometry("300x250")

    label = tk.Label(root, text="等待点击...",
                     font=("微软雅黑", 14), fg="gray")
    label.pack(pady=30)

    # command 参数绑定回调函数（函数名后面不加括号！）
    button = tk.Button(root, text="点我试试",
                       command=on_button_click, width=15,
                       font=("微软雅黑", 11), bg="#87CEEB")
    button.pack(pady=10)

    root.mainloop()


# ==========================================
# 示例 2: 回调函数带参数 (lambda)
# ==========================================
def demo_lambda_callback():
    """演示使用 lambda 给回调函数传参"""

    def update_label(text, color):
        label.config(text=text, fg=color)

    root = tk.Tk()
    root.title("lambda 回调传参")
    root.geometry("350x300")

    label = tk.Label(root, text="请选择一个操作",
                     font=("微软雅黑", 14))
    label.pack(pady=30)

    # 使用 lambda 传递参数
    tk.Button(root, text="数据清洗",
              command=lambda: update_label("正在执行数据清洗...", "green"),
              width=15, bg="#90EE90").pack(pady=5)

    tk.Button(root, text="生成图表",
              command=lambda: update_label("正在生成图表...", "blue"),
              width=15, bg="#87CEEB").pack(pady=5)

    tk.Button(root, text="重置",
              command=lambda: update_label("已重置", "gray"),
              width=15, bg="#E0E0E0").pack(pady=5)

    root.mainloop()


# ==========================================
# 示例 3: 餐厅类比 — 命令行 vs GUI
# ==========================================
def demo_restaurant_analogy():
    """
    餐厅类比可视化:
    - 命令行程序 = 你跑到厨房亲自告诉厨师每一步
    - GUI 程序 = 你坐在桌前对服务员说"蛋炒饭"
    """

    def order_dish(dish_name):
        log_text.insert(tk.END, f"【服务员】收到点餐: {dish_name}\n")
        log_text.insert(tk.END, f"【后  厨】正在制作 {dish_name}...\n")
        log_text.insert(tk.END, f"【服务员】{dish_name} 已上桌!\n\n")
        log_text.see(tk.END)

    root = tk.Tk()
    root.title("餐厅点餐类比 — 事件驱动")
    root.geometry("450x400")

    tk.Label(root, text="校园管家 — 餐厅点餐类比",
             font=("黑体", 14)).pack(pady=10)

    tk.Label(root, text="坐在桌前，点你想吃的 → 后厨自动完成",
             font=("微软雅黑", 10), fg="gray").pack()

    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=15)

    dishes = [
        ("数据清洗", "蛋炒饭", "#90EE90"),
        ("生成柱状图", "红烧肉", "#87CEEB"),
        ("生成饼图", "番茄汤", "#FFB6C1"),
        ("生成报告", "水果沙拉", "#FFFACD"),
    ]

    for gui_name, dish, color in dishes:
        tk.Button(menu_frame, text=f"点「{gui_name}」\n(={dish})",
                  command=lambda d=f"{gui_name}(={dish})": order_dish(d),
                  width=18, height=2, bg=color,
                  font=("微软雅黑", 9)).pack(pady=3)

    log_text = tk.Text(root, height=10, width=50,
                       font=("微软雅黑", 9), bg="#F5F5DC")
    log_text.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    print("事件驱动编程演示")
    print("1 - 基础回调函数")
    print("2 - lambda 传参")
    print("3 - 餐厅类比演示")
    choice = input("请选择 (1/2/3): ").strip()

    if choice == "1":
        demo_basic_callback()
    elif choice == "2":
        demo_lambda_callback()
    elif choice == "3":
        demo_restaurant_analogy()
    else:
        print("无效选择")
