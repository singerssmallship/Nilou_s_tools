"""
这是这个项目的主文件
功能是调用其他功能文件夹里面的py文件并使用其功能
"""
'''


'''

import ast
import importlib
import tkinter as tk
import os
import re
from PIL import Image, ImageTk
import ast
from itertools import islice
import importlib

def wdw_D1(x_=None,y_=None):
    root = tk.Tk()
    # ---------------------------------------------------窗口标题
    root.title('tools')
    # ---------------------------------------------------窗口位置,默认居中
    if x_ is None and y_ is None:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 360) // 2
        y = (screen_height - 360) // 2
        root.geometry('360x360+%d+%d' % (x, y))
    else:
        root.geometry('360x360+%d+%d' % (x_, y_))
    # ---------------------------------------------------窗口图标
    root.iconbitmap("necessary//icon.ico")
    # ---------------------------------------------------窗口背景颜色
    root['background'] = "white"
    # ---------------------------------------------------窗口背景图片
    img1 = tk.PhotoImage(file="necessary/D1_bg_picture.png")
    labe1_image1 = tk.Label(root,image=img1)
    labe1_image1.pack()
    # ---------------------------------------------------限制窗口被调整大小
    root.resizable(False, False)
    # ---------------------------------------------------按钮1
    def fuc_but_1():
        D1_x = root.winfo_x()
        D1_y = root.winfo_y()
        root.destroy()
        wdw_D1E1(D1_x,D1_y)

    button1 = tk.Button(root,
                        text="下载",
                        command=fuc_but_1,
                        bg="#cc9966",
                        font=("Microsoft YaHei",20),
                        height=1,
                        width=8)
    button1.place(x=180, y=30)
    root.bind('1', lambda event: fuc_but_1())        # 绑定快捷键1
    # ---------------------------------------------------按钮2
    def fuc_but_2():
        D1_x = root.winfo_x()
        D1_y = root.winfo_y()
        root.destroy()
        wdw_D1E2(D1_x,D1_y)
    button1 = tk.Button(root,
                        text="转换",
                        command=fuc_but_2,
                        bg="#cc9966",
                        font=("Microsoft YaHei",20),
                        height=1,
                        width=8)
    button1.place(x=180, y=115)
    root.bind('2', lambda event: fuc_but_2())  # 绑定快捷键2
    # ---------------------------------------------------按钮3
    def fuc_but_3():
        D1_x = root.winfo_x()
        D1_y = root.winfo_y()
        root.destroy()
        wdw_D1E3(D1_x,D1_y)
    button1 = tk.Button(root,
                        text="其他",
                        command=fuc_but_3,
                        bg="#cc9966",
                        font=("Microsoft YaHei",20),
                        height=1,
                        width=8)
    button1.place(x=180, y=200)
    root.bind('3', lambda event: fuc_but_3())  # 绑定快捷键3
    # ---------------------------------------------------按钮4
    def fuc_but_4():
        D1_x = root.winfo_x()
        D1_y = root.winfo_y()
        root.destroy()
        wdw_D1E4(D1_x,D1_y)
    button1 = tk.Button(root,
                        text="设置",
                        command=fuc_but_4,
                        bg="#cc9966",
                        font=("Microsoft YaHei",20),
                        height=1,
                        width=8)
    button1.place(x=180, y=285)
    root.bind('4', lambda event: fuc_but_4())  # 绑定快捷键4
    # ---------------------------------------------------
    root.mainloop()
def wdw_D1E1(x_=None,y_=None):
    '''
    这是一座屎山，功能是检测funcs文件夹里面有多少功能并显示在界面上方便选择
    但是tk我有点用不明白，到时候再直接修改
    :param x_:现在窗口的左上角x坐标
    :param y_:现在窗口的左上角x坐标
    :return:
    '''
    def FindFuncsList():
        '''
        读取settings.txt文件第二行的字符串
        :return: 第二行的列表（去掉开头
        '''
        #提取了settings文件里面的第二行的列表，用来作为传入给window_D1E1的功能列表
        with open('necessary\\settings.txt','r', encoding='utf-8') as file:
            second_line = ast.literal_eval(next(islice(file, 1, None))[6::])
            #print(second_line)
        return second_line

    def window_D1E1(FuncsList,x_=None,y_=None):
        '''

        :param FuncsList: 传入要检测到的funcs文件见里面的所有功能，然后显示再下拉栏里面
        :param x_: 现在窗口的左上角x坐标
        :param y_: 现在窗口的左上角x坐标
        :return:
        '''
        root = tk.Tk()
        # ---------------------------------------------------窗口位置,默认居中
        if x_ is None and y_ is None:
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width - 360) // 2
            y = (screen_height - 360) // 2
            root.geometry('360x360+%d+%d' % (x, y))
        else:
            root.geometry('360x360+%d+%d' % (x_, y_))
        # ---------------------------------------------------窗口颜色
        root['background'] = "#cc9966"
        # ---------------------------------------------------限制窗口被调整大小
        root.resizable(False, False)
        # ---------------------------------------------------创建框架frame，用来将下拉栏放在里面
        frame = tk.Frame(root, bg="blue", bd=0 , width=180 , height=360)
        frame.place(x=180 , y=0)
        # ---------------------------------------------------看一下下拉栏里面的内容
        print(FuncsList)
        # ---------------------------------------------------创建下拉栏，将FuncsList导入下拉栏
        listbox = tk.Listbox(frame,  font=("Microsoft YaHei", 20))
        for Func in FuncsList:  # 遍历水果列表，将每个水果添加到Listbox中
            listbox.insert(tk.END, Func)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        # ---------------------------------------------------定义函数，功能是按下后会加载并使用功能
        def OpenFunc(event):
            '''
            这是按下下拉栏后选择好功能后会执行的函数
            将会1导入写好的功能类
               2调用功能类并启动
            '''
            #获得func_name也就是将要用importlib导入的类
            func_name = 'funcs.Nstool_func_'+ FuncsList[int(str(listbox.curselection())[1])] +'.py'
            #摧毁当前窗口了
            root.destroy()
            try:
                #打开新窗口（不知道为什么直接就打开了新窗口，未来修）
                importlib.import_module(func_name)
            except:
                print("ERROR文件在窗口D1E1导入模块时出错")
        #绑定函数  OpenFunc  和双击左键和回车
        listbox.bind("<Double-Button-1>", OpenFunc)
        listbox.bind("<Return>", OpenFunc)

        # ---------------------------------------------------左上角返回按钮
        def button_return():
            D1_x = root.winfo_x()
            D1_y = root.winfo_y()
            root.destroy()
            wdw_D1(D1_x, D1_y)

        image = Image.open("necessary/All_button_return_picture.png")  # 图片的目录
        photo = ImageTk.PhotoImage(image)
        button_r = tk.Button(root, image=photo, command=button_return)
        button_r.place(x=10, y=10)
        root.mainloop()


    window_D1E1(FindFuncsList() )
def wdw_D1E2(x_=None,y_=None):
    root = tk.Tk()
    # ---------------------------------------------------窗口位置,默认居中
    if x_ is None and y_ is None:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 360) // 2
        y = (screen_height - 360) // 2
        root.geometry('360x360+%d+%d' % (x, y))
    else:
        root.geometry('360x360+%d+%d' % (x_, y_))
    # ---------------------------------------------------限制窗口被调整大小
    root.resizable(False, False)
    # ---------------------------------------------------按钮1到自带功能
    def fuc_but_1():
        D1_x = root.winfo_x()
        D1_y = root.winfo_y()
        root.destroy()

    button1 = tk.Button(root,
                        text="自带功能",
                        command=fuc_but_1,
                        bg="#cc9966",
                        font=("Microsoft YaHei",20),
                        height=1,
                        width=8)
    button1.place(x=180, y=30)
    # ---------------------------------------------------左上角返回按钮
    def button_return():
        D1_x = root.winfo_x()
        D1_y = root.winfo_y()
        root.destroy()
        wdw_D1(D1_x,D1_y)
    image = Image.open("necessary/All_button_return_picture.png")                  # 图片的目录
    photo = ImageTk.PhotoImage(image)
    button_r = tk.Button(root, image=photo, command=button_return)
    button_r.place(x=10, y=10)
    # ---------------------------------------------------
    root.mainloop()
def wdw_D1E3(x_=None,y_=None):
    root = tk.Tk()
    # ---------------------------------------------------窗口位置,默认居中
    if x_ is None and y_ is None:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 360) // 2
        y = (screen_height - 360) // 2
        root.geometry('360x360+%d+%d' % (x, y))
    else:
        root.geometry('360x360+%d+%d' % (x_, y_))
    # ---------------------------------------------------限制窗口被调整大小
    root.resizable(False, False)
    # ---------------------------------------------------
    root.mainloop()
def wdw_D1E4(x_=None,y_=None):
    root = tk.Tk()
    # ---------------------------------------------------窗口位置,默认居中
    if x_ is None and y_ is None:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 360) // 2
        y = (screen_height - 360) // 2
        root.geometry('360x360+%d+%d' % (x, y))
    else:
        root.geometry('360x360+%d+%d' % (x_, y_))
    # ---------------------------------------------------限制窗口被调整大小
    root.resizable(False, False)
    # ---------------------------------------------------
    root.mainloop()




if __name__ == '__main__':

    wdw_D1()