import os
import sys
import time
import pickle
import tkinter as tk
import tkinter.messagebox


from center_window import *


def upinquit():
    global usr_name   
    # 窗口
    window = tk.Tk()
    window['background']='wheat'
    window.title('五子棋注册登录界面')
    center_window(window,360,460)
    window.resizable(0,0)
    photo = tk.PhotoImage(file="img/dl.png")
    theLabel = tk.Label(window,
        text='',#内容
        justify=tk.CENTER,#对齐方式
        image=photo,#加入图片
        compound = tk.CENTER,#关键:设置为背景图片
        font=("华文行楷",20),#字体和字号
        fg = "white")#前景色
    theLabel.pack(fill='both',expand=1)
    # window.geometry('350x240')
    # 标签 用户名密码
    tk.Label(window, text='用户名:',background='#D3D6E3').place(x=70, y=190)
    tk.Label(window, text='密    码:',background='#D3D6E3').place(x=70, y=230)
    # 用户名输入框
    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name,)
    entry_usr_name.place(x=130, y=190)
    # 密码输入框
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*',)
    entry_usr_pwd.place(x=130, y=230)   

    # 登录函数
    def usr_log_in():
        global usr_name 
        # 输入框获取用户名密码
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        # 从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        # 判断用户名和密码是否匹配
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='welcome',
                                       message='欢迎您：'+usr_name)                   
                window.destroy()
                return usr_name        
            else:
                tk.messagebox.showerror(message='密码错误')
        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            tk.messagebox.showerror(message='用户名或密码为空')
        # 不在数据库中弹出是否注册的框
        else:
            is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
            if is_signup:
                usr_sign_up()

    # 注册函数
    photos = tk.PhotoImage(file="img/zc.png") 
    def usr_sign_up():
        # 确认注册时的相应函数
        def signtowcg():
            # 获取输入框内的内容
            nn = new_name.get()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()

            # 本地加载已有用户信息,如果没有则已有用户信息为空
            try:
                with open('usr_info.pickle', 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
            if nn in exist_usr_info:
                tk.messagebox.showerror('错误', '用户名已存在')
            elif np == '' or nn == '':
                tk.messagebox.showerror('错误', '用户名或密码为空')
            elif np != npf:
                tk.messagebox.showerror('错误', '密码前后不一致')
            # 注册信息没有问题则将用户名密码写入数据库
            else:
                exist_usr_info[nn] = np
                with open('usr_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo('欢迎', '注册成功')
                # 注册成功关闭注册框
                window_sign_up.destroy()
        # 新建注册界面
        window_sign_up = tk.Toplevel(window)
        center_window( window_sign_up,512,512)
        window_sign_up.title('注册')
        window_sign_up.resizable(0,0)     
        theLabels = tk.Label(window_sign_up,
            text='',#内容
            justify=tk.CENTER,#对齐方式
            image=photos,#加入图片
            compound = tk.CENTER,#关键:设置为背景图片
            font=("华文行楷",20),#字体和字号
            fg = "white")#前景色
        theLabels.pack()
        # 用户名变量及标签、输入框
        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='用     户    名：',font=("华文行楷",12),background='silver').place(x=100, y=160)
        tk.Entry(window_sign_up,font=("华文行楷",12), textvariable=new_name).place(x=250, y=160)
        # 密码变量及标签、输入框
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='密　　　码 ：',font=("华文行楷",12),background='silver').place(x=100, y=220)
        tk.Entry(window_sign_up,font=("华文行楷",12), textvariable=new_pwd, show='*').place(x=250, y=220)
        # 重复密码变量及标签、输入框
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='确 认 密 码 ：',font=("华文行楷",12),background='silver').place(x=100, y=280)
        tk.Entry(window_sign_up,font=("华文行楷",12), textvariable=new_pwd_confirm,
                 show='*').place(x=250, y=280)
        # 确认注册按钮及位置
        bt_confirm_sign_up = tk.Button(window_sign_up, text='注  　　  册',font=("华文行楷",12),
                                       command=signtowcg,background='silver')
        bt_confirm_sign_up.place(x=285, y=340)

    # 退出的函数
    def usr_sign_quit():
        global usr_name       
        window.destroy()
        usr_name = ''
        return usr_name 
        sys.exit(0)

    # 记住密码
    def remember_password():
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        if status.get()==1:            
            text.set('取消记住密码')
            usr_info = '%s %s'%(usr_name,usr_pwd)               
            with open('usr_info1.txt', 'wb') as usr_file1:
                usr_file1.write(usr_info.encode())        
        else:
            with open('usr_info1.txt', 'wb') as usr_file1:
                usr_file1.write(b'')
            text.set('记住密码')
            var_usr_name.set('')
            var_usr_pwd.set('')      
    # 自动登录   
    def automatic_login():
        global usr_name
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        if status1.get()==1:            
            text1.set('取消自动登录')
            usr_info = '%s %s ok'%(usr_name,usr_pwd)               
            with open('usr_info1.txt', 'wb') as usr_file1:
                usr_file1.write(usr_info.encode())
            usr_name = usr_log_in()
            return usr_name
        else:
            with open('usr_info1.txt', 'rb') as usr_file1:
                usrs_info = usr_file1.read().decode()
                l = usrs_info.split(' ')
                if ('ok' in l) and len(l) == 3:
                    del l[-1]
                    usr_info = ' '.join(l)               
                    with open('usr_info1.txt', 'wb') as usr_file1:
                        usr_file1.write(usr_info.encode())              
            text1.set('自动登录')  

    # 登录 注册按钮
    bt_login = tk.Button(window, text='登录', command=usr_log_in,background='#D3D6E3')
    bt_login.place(x=100, y=270)
    bt_logup = tk.Button(window, text='注册', command=usr_sign_up,background='#D3D6E3')
    bt_logup.place(x=170, y=270)
    bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit,background='#D3D6E3')
    bt_logquit.place(x=240, y=270)
    text=tk.StringVar()
    text.set('记住密码')
    status=tk.IntVar()
    text1=tk.StringVar()
    text1.set('自动登录')
    status1=tk.IntVar()
  
    ck1 = tk.Checkbutton(window, variable=status, command=remember_password,background='#D3D6E3')
    tk.Label(window,textvariable=text,background='#D3D6E3').place(x=125,y=310)
    ck2 = tk.Checkbutton(window, variable=status1, command=automatic_login,background='#D3D6E3')
    tk.Label(window,textvariable=text1,background='#D3D6E3').place(x=235,y=310)
    ck1.place(x=100, y=310)
    ck2.place(x=210, y=310)
    # 判断是否记住密码自动登录     
    with open('usr_info1.txt', 'rb') as usr_file1:
        usrs_info = usr_file1.read().decode()
        l = usrs_info.split(' ')     
        if usrs_info != '':                     
            var_usr_name.set(l[0])
            var_usr_pwd.set(l[1]) 
            ck1.select()           
            remember_password()                      
            if 'ok' in l: 
                ck2.select()
                automatic_login()     

    # 主循环
    window.mainloop()
    return usr_name
