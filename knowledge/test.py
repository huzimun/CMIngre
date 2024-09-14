import tkinter as tk
from tkinter import simpledialog

# 创建一个根窗口
root = tk.Tk()

# 弹出输入对话框
user_input = simpledialog.askstring("Input", "Enter your text:")

# 在后台接收用户输入
if user_input is not None:
    # 在这里可以对用户输入进行处理
    print("User input:", user_input)
else:
    print("User cancelled the dialog")

# 进入主循环
root.mainloop()
