import re
import tkinter as tk
import pyperclip
import webbrowser
import base64
import os


def judgeLink(url):
    reg1 = r'https://.+sharepoint\.com'
    reg2 = r'personal/(\w+?)/'
    reg3 = r'.*/(\S+)'
    reg4 = r'com/:(\w):/'

    p1 = re.findall(reg1, url)[0]
    p2 = re.findall(reg2, url)[0]
    p3 = re.findall(reg3, url)[0]

    if '?' in p3:
        p3 = re.findall(r'(\S+?)\?', p3)[0]

    if re.findall(reg4, url)[0] == 'f':
        return "抱歉，你所输入链接分享的是文件夹，直链生成仅对单文件有效。"

    return p1 + '/personal/' + p2 + '/_layouts/52/download.aspx?share=' + p3

def generate_link():
    url = url_entry.get()
    try:
        url_judged = judgeLink(url)       
        result_label.config(text=f"OneDrive直接链接为：{url_judged}")
    except Exception:
        result_label.config(text="输入链接错误，请重新输入。")

def copy_link():
    url_judged = result_label.cget("text").split("：")[1]
    pyperclip.copy(url_judged)

def open_blog():
    webbrowser.open_new_tab("https://www.0oo0.cc")

def open_github():
    webbrowser.open_new_tab("https://github.com/shuotianze/OneDriveSC")

# 创建窗口
window = tk.Tk()
window.title("OneDrive直链生成器")

# 获取屏幕尺寸
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 设置窗口位置居中
window.geometry("485x195+{}+{}".format(int((screen_width-485)/2), int((screen_height-195)/2)))

# 创建标签和输入框
url_label = tk.Label(window, text="请输入你的OneDrive单文件分享链接：")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# 创建直链和复制按钮
button_frame = tk.Frame(window)
button_frame.pack()
generate_button = tk.Button(button_frame, text="生成直链", command=generate_link)
generate_button.pack(side=tk.LEFT, padx=10, pady=10)
copy_button = tk.Button(button_frame, text="复制链接", command=copy_link)
copy_button.pack(side=tk.LEFT, padx=10, pady=10)


# 创建结果标签
result_label = tk.Label(window, text="", wraplength=400)
result_label.pack()

# 创建作者信息
writer = tk.Button(window, text="万能啊朔", command=open_blog)
writer.pack(side=tk.RIGHT, padx=10)
github = tk.Button(window, text="Github", command=open_github)
github.pack(side=tk.RIGHT, padx=10)
# 启动 GUI 应用程序
window.mainloop()

# 创建图标
tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode('图标的编码'))
tmp.close()
window.iconbitmap("tmp.ico")
os.remove("tmp.ico")  #删除icon文件 
