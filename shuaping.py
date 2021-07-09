import os
import time
import sys
import requests
import win32gui
import pyautogui
# # 窗口名
# hld = win32gui.FindWindow(None, u"XXXXXXXXXXXXX")
# win32gui.SetForegroundWindow(hld)
# 条数
for times in range(50):
    time.sleep(0.5)
    # 一言
    yiyan = str(requests.get('https://v1.hitokoto.cn/').json()['hitokoto'])
    # 毒鸡汤（搏天）
    dujitang = str(requests.get(
        'https://api.btstu.cn/yan/api.php?charset=utf-8&encode=json').json()['text'])
    # 诗句（一句）
    shiju = str(requests.get(
        'http://yijuzhan.com/api/word.php?m=json').json()['content'])

    def addToClipBoard(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)
    addToClipBoard(yiyan)
    num = num + 1
    pyautogui.hotkey('ctrl', 'v')
    pyautogui . hotkey('ctrl', 'enter')
