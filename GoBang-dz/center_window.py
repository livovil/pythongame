import tkinter

def center_window(window,ww,wh):
    #得到屏幕宽度
    sw = window.winfo_screenwidth()
    #得到屏幕高度  
    sh = window.winfo_screenheight()
    # 置窗口的x轴和y轴  
    x = (sw-ww) / 2
    y = (sh-wh) / 2
    window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

