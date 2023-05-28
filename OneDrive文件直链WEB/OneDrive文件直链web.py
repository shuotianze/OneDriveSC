import os
from flask import Flask, render_template, request
import re

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_judged = ""
        try:
            url = request.form['url']
            url_judged = judgeLink(url)
        except Exception:
            return render_template('index.html', error="输入链接错误，请重新输入。")
        return render_template('index.html', url=url_judged)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
