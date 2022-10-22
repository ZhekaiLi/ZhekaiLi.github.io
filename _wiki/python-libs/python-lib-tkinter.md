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
        self.CreateCanvas()
        self.CreateBotton()
        # other elements

    def CreateEntry(self):
        pass

    def CreateCanvas(self):
        pass

    def CreateBotton(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry(f'{300}x{900}')
    app = Application(master=root)
    root.mainloop()
```

# 控件