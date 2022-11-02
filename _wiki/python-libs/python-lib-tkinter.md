---
layout: wiki
title: tkinter
cate1: Python
cate2: -libs
description: 
keywords: Python
---

# Code Framework 代码框架
```py
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.CreateEntry()
        self.CreatePicture()
        self.CreateBotton()
        # other elements

    def CreateEntry(self):
        pass

    def CreatePicture(self):
        pass

    def CreateBotton(self):
        # 创建按钮对象
        self.B = Button(self, text="Button_1", command=Bt_function)
        # 定位
        self.B.grid(row=0, column=0, rowspan=1, columnspan=1)

    def Bt_function(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry(f'{300}x{900}')
    app = Application(master=root)
    root.mainloop()
```

# Elements
```py
from tkinter import *
tk = Tk()
```

## Label
显示文字标签
```py
lb = Label(tk, text="Text Content")
```

显示图片标签
```py
pic = PhotoImage(file="pic.png")
lb_pic = Label(tk, image=pic)
```

## Entry
输入框
```py
# 定义一个字符串变量，用于接收输入
v = StringVar()
# 定义一个长度为 10 个字符的输入框
ety = Entry(tk, textvariable=v, width=10) 
```

## Botton
创建按钮，并绑定触发事件
```py
B = Button(tk, text="Botton", command=Bt_function)

def Bt_function:
    pass
```

