import sys
import pickle
import tkinter as tk
import tkinter.messagebox


from center_window import *


def main_info():
    global choose 
    # 窗口
    window = tk.Tk()
    window.title('主菜单')
    window.resizable(0,0)
    window['background']='wheat'
    center_window(window,335,667)
    photo = tk.PhotoImage(file="img/main.png")
    theLabels = tk.Label(window,
        text='',#内容
        justify=tk.CENTER,#对齐方式
        image=photo,#加入图片
        compound = tk.CENTER,#关键:设置为背景图片
        font=("华文行楷",20),#字体和字号
        fg = "white")#前景色
    theLabels.pack()
   


    # 登录函数
    def playgobang():
        global choose
        choose = 'play'             
        window.destroy()
        return choose 

    def switch_user():
        global choose
        choose = 'switch_user'             
        window.destroy()
        return choose     

    # 退出的函数
    def usr_sign_quit():
        global choose
        choose = 'quit'
        window.destroy()
        return choose 

    # 游戏规则
    def rule():
        global choose
        choose = 'rule'
        window.destroy()
        return choose 
             

    # 游戏　注销
    bt_login = tk.Button(window, text='游  戏  规  则', font=("华文行楷",18),command=rule,background='tan')
    bt_login.place(x=100, y=160)
    bt_login = tk.Button(window, text='人  机  对  战', font=("华文行楷",18),command=playgobang,background='tan')
    bt_login.place(x=100, y=270)
    bt_login = tk.Button(window, text='切  换  用  户', font=("华文行楷",18),command=switch_user,background='tan')
    bt_login.place(x=100, y=380)
    bt_logquit = tk.Button(window, text='注        销', font=("华文行楷",18),command=usr_sign_quit,background='tan')
    bt_logquit.place(x=115, y=490)
    # 主循环
    window.mainloop()
    return choose




