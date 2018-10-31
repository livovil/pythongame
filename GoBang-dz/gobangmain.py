#!/usr/bin/env python3
from __future__ import unicode_literals
# -*- coding:utf-8 -*-

'''
Team:  缔造者
Team members: 李福坤　刘大汗　向潮　刘英宁  冯炜晁  杨宁  肖遥    　
email: lifuk1993@163.com
date:  2018 - 10
class: AID1807
introduce: Gobang
env : python3.5  
'''

import os
import sys
import pickle
import signal
import tkinter as tk
import tkinter.messagebox
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox


from up_in_quit import *
from mainfo import *
from gobangGUI import *
from rule import *
from center_window import *


def sig_he(fid):
    ppid = os.getppid()
    n = 1
    while True:
        time.sleep(3600)
        if ppid != os.getppid():
            break
        top = tk.Tk()
        center_window(top, 10, 10)
        if n <= 3:
            tkinter.messagebox.showinfo(title='温馨提示',
                                        message='您已游戏%d小时！' % n)
        elif n < 5:
            tkinter.messagebox.showinfo(title='温馨提示',
                                        message='您已游戏%d小时，请注意身体健康！' % n)
        elif n >= 5:
            tkinter.messagebox.showwarning(title='警告！',
                                           message='您已游戏%d小时，十分钟后系统将自动关闭！' % n)

            time.sleep(0.01)
            top.destroy()
            time.sleep(600)
            os.kill(fid, signal.SIGKILL)
            break

        n += 1
        time.sleep(0.01)
        top.destroy()


def pmain():
    while True:
        # 登录
        up_msg = upinquit()
        if up_msg == '':
            os.kill(pid, signal.SIGKILL)
            sys.exit(0)
        else:
            while True:
                # 主菜单
                mainfo_msg = main_info()
                # 人机对战
                if mainfo_msg == 'play':
                    app = QApplication(sys.argv)
                    ex = GoBang(up_msg)
                    app.exec_()
                # 切换用户
                elif mainfo_msg == 'switch_user':
                    with open('usr_info1.txt', 'wb') as message:
                        message.write(b'')
                    break
                # 退出
                elif mainfo_msg == 'quit':
                    os.kill(pid, signal.SIGKILL)
                    sys.exit(0)
                elif mainfo_msg == 'rule':
                    rules()


def main():
    global pid
    pid = os.fork()
    if pid < 0:
        sys.exit(0)
    elif pid == 0:
        fid = os.getppid()
        sig_he(fid)
        time.sleep(0.5)
    else:
        pmain()
if __name__ == '__main__':
    main()
