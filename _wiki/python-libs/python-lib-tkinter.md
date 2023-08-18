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

# Tk
main GUI

```py
import tkinter as tk

main = tk.Tk()
main.title("Title")            # 设置窗口标题
main.geometry(f'{300}x{900}')  # 设置窗口大小
main.config(bg="#fff")         # 设置背景色为白色

main.mainloop()                # 运行窗口
```

---

# Botton
按钮, 可以放进 Tk, Frame, 或 Canvas 中

```py
def Bt_function:
    pass

# 创建按钮，并绑定触发事件
btn = tk.Button(canvas, text="Botton", command=Bt_function)
# 设置按钮的大小和按下去时的样式
btn.configure(width=10, height=2, activebackground="#33B5E5", relief=tk.FLAT)
# 设置按钮的位置
btn_window = canvas.create_window(10, 10, anchor=tk.NW, window=btn)
btn.pack(side='top')
```

在创建按钮时，使用 `lambda` 传递参数

```py
B = tk.Button(tk, text="Botton", command=lambda: Bt_function(arg1, arg2))
```



# Canvas

添加一块画布区域

```python
canvas = tk.Canvas(main, with=1300, height=350, bg="white")
canvas.pack(side=tk.TOP) # 设置画布在顶部（此时如果前面已经有一个 frame.pack(side=tk.TOP)，那么画布会跟在框架后面）

# OPTIONAL
# (1) 固定画布的大小，防止元素过多时画布自动扩展，或元素过少时画布自动收缩
canvas.pack_propagate(0)
```


# Entry
输入框, 可以放进 Tk, Frame, 或 Canvas 中

```py
# 定义一个字符串变量，用于接收输入
v = StringVar()
# 定义一个长度为 10 个字符的输入框
ety = Entry(main, textvariable=v, width=10) 
```



# FigureCanvasTkAgg
在 tkinter 中显示 matplotlib 的图像

```py
fig, axs = plt.subplots(2, 2, figsize=(14, 2.4), dpi=72)

figCanvas = FigureCanvasTkAgg(fig_utilization, master=main)
figCanvas.get_tk_widget().config(height = 240)
figCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
```


# Frame
添加一块框架区域，用于放置各种元素

```python
top_frame = tk.Frame(main, width=1300, height=85, bg="white")
top_frame.pack(side='top', # 设置框架在顶部 
               fill='x',   # 在水平方向上填充窗口
               anchor='nw',# 设置框架的锚点为左上角
               expand=True)

# OPTIONAL
# (1) 固定框架的大小，防止元素过多时框架自动扩展，或元素过少时框架自动收缩
top_frame.pack_propagate(0)
```

初始化完框架区域后，需要进步设置框架区域的大小和颜色，并放置元素。例如，在蓝色背景上放置一个 logo:

```python
logo = PhotoImage(file="logo.png") # 读取图片
tk.Label(top_frame, image=logo, bg="#1f77b4", height=85, width=1300).pack() # 在框架中添加元素
```

## Frame + Scrollbar
<span style="background-color: yellow; color: black;">为 frame 创建 scrollbar 的过程十分的复杂</span>，需要在目标 frame 外部先套一层 canvas，再套一层 frame。以下每一步的顺序都不能出错：
1. 创建最外层的 frame，记作 `frame_canvas`
2. 创建 scrollbar，绑定与 `frame_canvas`
3. 创建外层 canvas，绑定与 `frame_canvas` + scrollbar
4. 配置 scrollbar，绑定与 canvas
5. 创建目标 frame，绑定与 canvas，记作 `frame_target`
6. 往 `frame_target` 中添加元素
7. 根据添加元素后 `frame_target` 的大小，设置 scrollbar 的滑动范围

```py
# (1) 创建最外层的 frame 
frame_canvas = tk.Frame(main, width=500, height=500)
frame_canvas.pack(side='top', fill='x', anchor='nw')

# (2) 创建 scrollbars，绑定与 frame
sby = tk.Scrollbar(self.frame_canvas, orient='vertical')
sby.pack(side='right', fill='y')
sbx = tk.Scrollbar(self.frame_canvas, orient='horizontal')
sbx.pack(side='bottom', fill='x')

# (3) 创建外层 canvas，绑定与 frame + scrollbars
canvas = tk.Canvas(frame_canvas, yscrollcommand=sby.set, xscrollcommand=sbx.set)
canvas.pack(side='left', fill='both')

# (4) 配置 scrollbars，绑定与 canvas
sby.config(command=canvas.yview)
sbx.config(command=canvas.xview)

# (5) 创建目标 frame，绑定与 canvas
frame_target = tk.Frame(canvas)
canvas.create_window((0, 0), window=self.frame_target, anchor='nw')

# (6) 往目标 frame 中添加元素
# ...

# (7) 根据添加元素后目标 frame 的大小，设置 scrollbar 的滑动范围
frame_target.update_idletasks()
frame_target.update()
canvas.config(scrollregion=(0, 0, self.frame.winfo_width(), self.frame.winfo_height()))
```

实现效果如下


<img src="/images/2023-05/Snipaste_2023-08-08_15-45-31.png" width="80%">


# Label
显示文字标签, 可以放进 Tk, Frame, 或 Canvas 中

```python
lb = tk.Label(main, text="Text Content")
     tk.Label(frame, text="Text Content")
     tk.Label(canvas, text="Text Content")
```
显示图片标签

```py
pic = PhotoImage(file="pic.png")
lb_pic = Label(main, image=pic)
```



# Listbox
列表，可以逐行显示文字

```py
loglist = tk.Listbox(frame, height=10, bg="white")
# 需要注意的是这里的 height 是指显示的行数，而不是列表的高度
loglist.pack(side='left')

loglist.insert(tk.END, "Text Content")
```

## Listbox + Scrollbar
<span style="background-color: yellow; color: black;">
注意！</spam>

- <span style="background-color: yellow; color: black;">Scrollbar 必须声明在 Listbox 之前，不然可能会导致无法显示</spam>



```py
sby = tk.Scrollbar(frame, orient=tk.VERTICAL)
sby.pack(side='right', fill='y')

loglist = tk.Listbox(frame, ..., yscrollcommand=sby.set)
loglist.pack(side='left')
sby.config(command=loglist.yview)
```



# Toplevel
创建一个新的窗口，常绑定到按钮上，从而实现 "点击按钮后弹出新窗口" 的功能

```py
def new_window():
    toplevel = Toplevel()
    toplevel.title("New Window")
    toplevel.geometry(f'{300}x{300}')
    toplevel.config(bg="#fff")

    # 设置关闭按钮的功能（当点击窗口的关闭键后，销毁窗口）
    def on_close():
        toplevel.destroy()
    toplevel.protocol("WM_DELETE_WINDOW", on_close)

root = Tk()
button = Button(root, text="New Window", command=new_window)
button.pack()
root.mainloop()
```

## Toplevel + SimPy
当 Toplevel 结合 SimPy 来使用时，我们往往会希望在打开一个窗口时开始一个进程 `env.process()`，并且在关闭这个窗口时结束这个进程，从而避免资源浪费。示例如下:

```py
class tkUpdate:
    def __init___(self, env, canvas):
        self.env = env
        self.canvas = canvas

    def run(self):
        while True:
            if self.canvas is not None and self.canvas.winfo_exists():
                # do something change on canvas
         env.timeout(1)

def create_toplevel():
    toplevel = Toplevel()
    toplevel.title("New Window")

    canvas = Canvas(toplevel, width=700, height=240)

    # Start the SimPy process when the Toplevel window is opened
    tkU = tkUpdate(env, canvas)
    process = env.process(tkU.run())

    # Bind the <WM_DELETE_WINDOW> event to a function that stops the SimPy process
    def on_close():
        process.interrupt((simpy.events.Event("Window closed")))
        toplevel.destroy()
    toplevel.protocol("WM_DELETE_WINDOW", on_close)

env = simpy.Environment()
root = tk.Tk()
button = tk.Button(root, text="Create Toplevel", command=create_toplevel)
button.pack()
root.mainloop()
```

