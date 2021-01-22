import requests
import os
import time
import pyautogui, sys
import win32gui
# 请选择（输入数字选择）：1、一言；2、毒鸡汤（搏天）；3、诗句（一句）
x = 3
num = 1
# 窗口名
hld = win32gui.FindWindow(None, u"XXXXXXXXXXXXX")
win32gui.SetForegroundWindow(hld)
# 条数
while num <= 50:
    time.sleep(0.5)
    # 一言
    o = str(requests.get('https://v1.hitokoto.cn/').json()['hitokoto'])
    # 毒鸡汤
    p = str(requests.get(
        'https://api.btstu.cn/yan/api.php?charset=utf-8&encode=json').json()['text'])
    # 诗句
    s = str(requests.get(
        'http://yijuzhan.com/api/word.php?m=json').json()['content'])
    if x == 1:
        bbb = o
    if x == 2:
        bbb = p
    if x == 3:
        bbb = s
    def addToClipBoard(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)
    addToClipBoard(bbb)
    num = num + 1
    pyautogui.hotkey('ctrl', 'v')
    pyautogui . hotkey('ctrl', 'enter')
