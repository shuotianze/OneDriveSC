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
# 创建图标
tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode('AAABAAEAEBAAAAEAGABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAAAAMQOAADEDgAAAAAAAAAAAAD+/v7+/v7+/v7+/v7+/v6oqvG9uepiW2j189vx9Nv18d7K0ez38d7y7tz179i9x/b+/v7+/v7+/v7+/v7+/v5uY4P38+HCvtfz9uDa0b3v7dvQ1+v19ub59d1bVHXCyer+/v7+/v7+/v7+/v7+/v7Y1Kvr5NDT2+z29eH28uf49OHT1+9ISFrh5u+pqvT//P/+/v7+/v7+/v7+/v7+/v7Z1K3k38DU2+z09OKpuvKxv/TW3OnU2+ynqfCmqO9zc4H+/v7+/v7+/v7+/v7//f/g6/l/eXrT1eepsO9BPFmmvvKprfzU1uDS2eqpq/L+/v7+/v7+/v7+/v7+/v7X4fni6/jX2/Pc5vji6/insPna4/fR1/rU2+zW2vaxpdn+/v7+/v7+/v7+/v55eX/i6/i+v9TGz/vL1PpPTIOfpuvW3/rJz/rY2OrU2u1taZP19Pb+/v7+/v7+/v7h6vf+/v7X2+1HSXHM1v7f5P3g7PjBzenP1vHO1OfU2+zT2utOUl3+/v7+/v6JjZji6/n+/v7U2+zT1+nc5vjc6ffU2+ze6/ni6/jU3O3V3e7U2+y0qOr+/v7+/v7i6/j+/v55dYHV3O3W3e7c3/uxo/vV3e7V3O3T2uvY3/DW3u/W3u9OTGn+/v7+/v7e6vb18f3+/v7+/v7W3ezW3+2qovnW3+3L0uHY5+rX4O7W3+3Y4e/+/v7+/v7+/v7K1/f+/v7+/v7+/v5oZHDd9/3Z4vDa4fLX4O7Z4vDX4O7W3+3Y3+7+/v7+/v7+/v5dZIX+/v7+/v7+/v7P2eOPlp/Y4e/X4O7Z4vDa4/Ha4/Fsbnb+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v59fojX4O7+/v6uq/D+//3+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7////Y4e/Z4O/d5PP+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v76+PfV3O39//7+/v7+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))
tmp.close()
window.iconbitmap("tmp.ico")
os.remove("tmp.ico")  #删除icon文件

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

