import re

first_run = True  # 添加一个布尔型变量
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

if __name__ == "__main__":
    while True:
        try:
            if first_run:  # 第一次运行时输出提示语句
                print("作者万能的啊朔，了解更多访问：www.sdax.top")
                first_run = False
            
            url = input("请输入你的OneDrive单文件分享链接：")
            url_judged = judgeLink(url)
            print(f"\nOneDrive直接链接为：{url_judged}\n")
        except Exception:
            print("\n>>> 输入链接错误，请重新输入。")
            continue
