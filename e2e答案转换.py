import tkinter as tk
from tkinter import messagebox

def process_input():
    n = entry.get()
    a = len(n)
    result = []
    for i in range(a):
        if n[i] == '1':
            b = 'A'
        elif n[i] == '2':
            b = 'B'
        elif n[i] == '3':
            b = 'C'
        else:
            b = 'D'
        result.append(b)
    # 每五个答案字符换行
    formatted_result = ''
    for i in range(0, len(result), 5):
        formatted_result += ','.join(result[i:i+5]) + '\n'
    messagebox.showinfo("结果", "本套选择题的答案为:\n" + formatted_result.strip())

root = tk.Tk()
root.title("E2E选择题答案转化工具")
tk.Label(root, text="本工具便于快速转换选择题答案,仅供学习交流使用.").pack(padx=40, pady=20)
tk.Label(root, text="请输入var answer指向的内容:").pack(padx=40, pady=20)
entry = tk.Entry(root)
entry.pack(padx=100, pady=25)

tk.Button(root, text="显示转换后的答案", command=process_input).pack(padx=10, pady=10)

root.mainloop()