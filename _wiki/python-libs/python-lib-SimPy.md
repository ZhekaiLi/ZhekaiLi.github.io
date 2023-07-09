---
layout: wiki
title: SimPy
cate1: Python
cate2: -libs
description: 
keywords: Python
---

```py
import simpy
```

# 1. Components
## 1.1 Environment
核心中的核心，是用来承载一切模拟的环境

```py
env = simpy.Environment() # 创建一个环境
proc1 = env.process(func) # 添加一个进程
```

## 1.2 Container
容器，用于存放物品

```py
# 创建一个容量为 1000 的容器，初始容量为 500
Con1 = simpy.Container(env, capacity=1000, init = 500)

Con1.get(100) # 从容器中取出 100 个 
print(Con1.level) # 查看容器中的剩余量 --> 400
Con1.put(200) # 向容器中放入 200 个
print(Con1.level) # 查看容器中的剩余量 --> 600
```

## 1.3 Resource
资源，可以用来表示机器、人员等。其特点在于一个资源同时只能被一个进程占用。因此更适用于表示流水线上的机器，或者是服务设施中的服务员:
- 汽车生产流水线上的机器
- 电影院中的售票员

```py
# Create a workstation (with 3 parallel machines)
workstation = simpy.Resource(env, capacity=3)

# Request a machine from the workstation
with workstation.request() as req:
    # Wait until one of the machines is available (如果三台机器都被占用，则会持续等待)
    yield req
    process_time = 1
    # 执行机器操作
    yield env.process(process_function())
```

### Mutex-Lock
由于一个资源同时只能被一个进程占用的特性，我们可以直接拿它来作为 Mutex-Lock。例如，对于列表 `reservation = [...]`，我们希望任意时刻最多只有一个函数能够修改它:

```py
reservation = [...]
reservation_R = simpy.Resource(env, capacity=1)

def func_1(resv, resv_R):
    with resv_R.request() as req:
        # change resv here
        pass

def func_2(resv, resv_R):
    with resv_R.request() as req:
        # change resv here
        pass
```

更多信息可以参考 [Simulating Dining Philosophers with SimPy](https://towardsdatascience.com/simulating-dining-philosophers-with-simpy-5abf5106e2ca)


### Alternatives

对于更传统的工厂 (reentrancy 较高，例如 fac), 或者那种更关注于流程而不是每个资源个体的, 可以使用如下代码来模拟 machine & workstation:

```py
# Create a machine
def machine(env, con1, con2):
    while True:
        # get 2 inputs from Container_1
        yield con1.get(2)
        # after 1 time processing
        yield env.timeout(1)
        # put 1 output into Container_2
        yield con2.put(1)

# Create a workstation (with 3 parallel machines)
def workstation(env, num_machines, con1, con2):
    for i in range(3):
        env.process(machine(env, con1, con2))
```




# Example: Guitar Factory
**吉他工厂**: 使用木头和电子元件作为原材料，经过加工和组装后，生产出吉他。

## .1 One Machine
最简单的工厂: 一台机器，使用一种原材料，生产一种产品。

<center><img src="/images/2023-03/Snipaste_2023-04-14_23-33-39.png"  width="70%"></center>

```py
# Containers
    # crude container
crudeCon_capacity = 1000
crudeCon_initial = 500
    # product container
prodCon_capacity = 500
#-------------------------------------------------
class Factory:
    def __init__(self, env):
        self.env = env
        
        # 定义两个容器 (Container)
        # 一个用来存放原材料，一个用来存放加工后的材料
        self.crudeCon = simpy.Container(env, capacity=crudeCon_capacity, init = crudeCon_initial)
        self.prodCon = simpy.Container(env ,capacity = prodCon_capacity, init = 0)
        
    # 定义一台 machine
    # [流程]: 从原料勇气中取出 2 个原材料，加工成 1 个产品，并放入产品容器
    # [时间]: 1 个时间单位
    def maker(self):
        while True:
            yield self.crudeCon.get(2)
            process_time = 1
            yield self.env.timeout(process_time)
            yield self.prodCon.put(1)
#-------------------------------------------------
# 创建环境、工厂对象
env = simpy.Environment()
factory = Factory(env)
# 添加一台 machine
env.process(factory.maker())
# 模拟到第 50 个时间单位
env.run(until = 50)

print(f'%d products are finished!' % factory.prodCon.level)
```

**Output**: `250 products are finished!`



## .2 Parallel Machines (A Guitar Factory)

<center><img src="/images/2023-03/Snipaste_2023-04-15_12-21-28.png"  width="90%"></center>

```py
class Guitar_Factory:
    def __init__(self, env):
        self.env = env
        
        # 定义五个容器 (Container)
        self.woodCon = simpy.Container(env, capacity=1000, init = 500)
        self.prePaintCon = simpy.Container(env, capacity=100, init = 0)
        self.postPaintCon = simpy.Container(env, capacity=200, init = 0)
        self.elecCon = simpy.Container(env, capacity=100, init = 100)
        self.guitarCon = simpy.Container(env ,capacity=500, init = 0)
        
    # 定义三台 machine
    # maker: 加工木头，制作成琴身
    def maker(self):
        while True:
            yield self.woodCon.get(2)
            process_time = 1
            yield self.env.timeout(process_time)
            yield self.prePaintCon.put(1)
    # painter: 为琴身涂漆
    def painter(self):
        while True:
            yield self.prePaintCon.get(1)
            process_time = 4
            yield self.env.timeout(process_time)
            yield self.postPaintCon.put(1)
    # assembler: 组装琴身、电子元件，制作成吉他
    def assembler(self):
        while True:
            yield self.postPaintCon.get(1)
            yield self.elecCon.get(1)
            process_time = 1
            yield self.env.timeout(process_time)
            yield self.guitarCon.put(1)
#-------------------------------------------------
# 创建环境、工厂对象
env = simpy.Environment()
factory = Guitar_Factory(env)
# 添加三台 machine
env.process(factory.maker())
env.process(factory.painter())
env.process(factory.assembler())
# 模拟到第 50 个时间单位
env.run(until = 50)

print(f'Pre-paint Container has %d bodies ready to be painted' % factory.prePaintCon.level)
print(f'Post-paint Container has %d bodies ready to be assembled' % factory.postPaintCon.level)
print(f'%d products are finished!' % factory.guitarCon.level)
```

## .3 More Advanced

**更加完整的吉他工厂**:
- 加工时间服从正态分布
- workstation 中可以有多台 parallel machines
- <span style="background-color: yellow; color: black;">库存报警 + 订货</span>: 当 wood or elec Containor 的库存量低于某个值时，触发报警装置，同时联系供应商订货

<center><img src="/images/2023-03/Snipaste_2023-04-16_17-56-10.png"  width="95%"></center>

### .3.1 Variable Processing Time

以 `maker` 为例，之前加工一个产品的时间为 1 个时间单位。现在假设加工时间服从正态分布 $N(1, 0.2)$。

```py
def maker(self):
    while True:
        yield self.woodCon.get(2)
        process_time = random.gauss(1, 0.2) # 调用 random 库
        yield self.env.timeout(process_time)
        yield self.prePaintCon.put(1)
```

### .3.2 Multiple Machines in One Workstation

以 `maker` 为例，之前只有一个机器把木材加工为琴身。现在假设有两台并行的机器同时加工木材

```py
num_maker = 2 # 两台机器
def makerGen(self): # maker Generator
    for i in range(num_maker):
        yield self.env.process(self.maker())
```

### .3.3 Stock Alarm (库存报警装置)

以 `woodCon` 为例，当木材容器的库存量低于 100 时:
- 触发报警装置
- 同时联系木材供应商，购买 300 个木材 (leadtime = 16)

```py
wood_critial_stock = 100
def wood_stock_control(self):
    yield self.env.timeout(0)
    while True:
        if self.woodCon.level <= wood_critial_stock:
            # 触发警报
            print('Wood stock bellow critical level ({0}) at time {1}'.\
                format(self.woodCon.level, int(self.env.now)))
            # 联系供应商，购买 300 个木材
            print('Calling wood supplier...')
            yield self.env.timeout(16)
            print('Wood supplier arrives at time {0}'.format(int(self.env.now)))
            yield self.woodCon.put(300)
            print('New wood stock is {0}'.format(self.woodCon.level))
            # 进货一次之后，至少再等 8 个时间单位才能重新检查库存
            yield self.env.timeout(8)
        else:
            # 如果没有触发警报，就每隔 1 个时间单位检查一次库存
            yield self.env.timeout(1)
```

### .3.4 完整代码

```py
# Number of parallel machines
num_maker = 2
num_painter = 3
num_assembler = 1

# Critial Stock Level (when reach 触发警报并订货)
wood_critial_stock = 100
wood_order_amount = 300
wood_order_leadTime = 16

elec_critial_stock = 30
elec_order_amount = 50
elec_order_leadTime = 8 

class Guitar_Factory:
    def __init__(self, env):
        self.env = env
        
        # 五个容器 (Container)
        self.woodCon = simpy.Container(env, capacity=1000, init = 500)
        self.prePaintCon = simpy.Container(env, capacity=100, init = 0)
        self.postPaintCon = simpy.Container(env, capacity=200, init = 0)
        self.elecCon = simpy.Container(env, capacity=100, init = 100)
        self.guitarCon = simpy.Container(env ,capacity=1000, init = 0)
    # -----------------------------------------------------
    # Machines
    # maker: 加工木头，制作成琴身
    def maker(self):
        while True:
            yield self.woodCon.get(2)
            process_time = random.gauss(1, 0.2)
            yield self.env.timeout(process_time)
            yield self.prePaintCon.put(1)
    # painter: 为琴身涂漆
    def painter(self):
        while True:
            yield self.prePaintCon.get(1)
            process_time = random.gauss(4, 1)
            yield self.env.timeout(process_time)
            yield self.postPaintCon.put(1)
    # assembler: 组装琴身、电子元件，制作成吉他
    def assembler(self):
        while True:
            yield self.postPaintCon.get(1)
            yield self.elecCon.get(1)
            process_time = 1
            yield self.env.timeout(process_time)
            yield self.guitarCon.put(1)  
    # -----------------------------------------------------
    # Machine Generator: 生成多个 parallel machines
    def makerGen(self): # maker Generator
        for i in range(num_maker):
            yield self.env.process(self.maker())
    def painterGen(self): # painter Generator
        for i in range(num_painter):
            yield self.env.process(self.painter())
    def assemblerGen(self): # assembler Generator
        for i in range(num_assembler):
            yield self.env.process(self.assembler())
    # -----------------------------------------------------
    # 定义库存报警
    def wood_stock_control(self):
        yield self.env.timeout(0)
        while True:
            if self.woodCon.level <= wood_critial_stock:
                # 触发警报
                print('Wood stock bellow critical level ({0}) at time {1}'.\
                    format(self.woodCon.level, int(self.env.now)))
                # 联系供应商，购买 300 个木材
                print('Calling wood supplier...')
                yield self.env.timeout(wood_order_leadTime)
                print('Wood supplier arrives at time {0}'.format(int(self.env.now)))
                yield self.woodCon.put(wood_order_amount)
                print('New wood stock is {0}'.format(self.woodCon.level))
                print('------------------------------------------')
                # 进货一次之后，至少再等 8 个时间单位才能重新检查库存
                yield self.env.timeout(8)
            else:
                # 如果没有触发警报，就每隔 1 个时间单位检查一次库存
                yield self.env.timeout(1)
    
    def elec_stock_control(self):
        yield self.env.timeout(0)
        while True:
            if self.elecCon.level <= elec_critial_stock:
                print('Elec stock bellow critical level ({0}) at time {1}'.\
                    format(self.elecCon.level, int(self.env.now)))
                print('Calling elec supplier...')
                yield self.env.timeout(16)
                print('Elec supplier arrives at time {0}'.format(int(self.env.now)))
                yield self.elecCon.put(50)
                print('New elec stock is {0}'.format(self.elecCon.level))
                print('------------------------------------------')
                yield self.env.timeout(8)
            else:
                yield self.env.timeout(1)

# 创建环境、工厂对象
env = simpy.Environment()
factory = Guitar_Factory(env)
# Add machines
env.process(factory.makerGen())
env.process(factory.painterGen())
env.process(factory.assemblerGen())
# Add alarm and replenishment
env.process(factory.wood_stock_control())
env.process(factory.elec_stock_control())
# Simulate to time 500
env.run(until = 500)

print(f'Pre-paint Container has %d bodies ready to be painted' % factory.prePaintCon.level)
print(f'Post-paint Container has %d bodies ready to be assembled' % factory.postPaintCon.level)
print(f'%d products are finished!' % factory.guitarCon.level)
```

**Output**:

```c
Elec stock bellow critical level (30) at time 289
Calling elec supplier...
Elec supplier arrives at time 305
New elec stock is 77
------------------------------------------
Wood stock bellow critical level (100) at time 398
Calling wood supplier...
Wood supplier arrives at time 414
New wood stock is 394
------------------------------------------
Elec stock bellow critical level (30) at time 491
Calling elec supplier...
Pre-paint Container has 100 bodies ready to be painted
Post-paint Container has 0 bodies ready to be assembled
121 products are finished!
```



## .4 Dispatch Production

我们还需要监测生产完成的吉他数量。如果库存量超过 50，就联系 retailor 来取货

```py
def guitar_stock_control(self):
        # 声明一个全局变量，来记录生产的吉他总数
        global guitars_made
        yield self.env.timeout(0)
        while True:
            if self.guitarCon.level >= 50:
                print('Guitar Containor stock is {0}, calling store to pick guitars at time {1}'.format(self.guitarCon.level, int(env.now)))
                yield env.timeout(4)
                print('Store picking {0} guitars at day time {1}'.format(self.guitarCon.level, int(env.now)))
                guitars_made += self.guitarCon.level
                yield self.guitarCon.get(self.guitarCon.level)
                print('----------------------------------')
                yield env.timeout(8)
            else:
                yield env.timeout(1)
```

最后，把 stock alarm (control) 加入到 `__init__` 函数中。完整代码如下:

```py
# Number of parallel machines
num_maker = 2
num_painter = 3
num_assembler = 1

# Critial Stock Level (when reach 触发警报并订货)
wood_critial_stock = 100
wood_order_amount = 300
wood_order_leadTime = 16

elec_critial_stock = 30
elec_order_amount = 50
elec_order_leadTime = 8 

class Guitar_Factory:
    def __init__(self, env):
        self.env = env
        
        # 五个容器 (Container)
        self.woodCon = simpy.Container(env, capacity=1000, init = 500)
        self.woodControl = env.process(self.wood_stock_control())
        self.elecCon = simpy.Container(env, capacity=100, init = 100)
        self.elecControl = env.process(self.elec_stock_control())

        self.prePaintCon = simpy.Container(env, capacity=100, init = 0)
        self.postPaintCon = simpy.Container(env, capacity=200, init = 0)
        
        self.guitarCon = simpy.Container(env ,capacity=1000, init = 0)
        slef.guitarControl = env.process(self.guitar_stock_control())
    # -----------------------------------------------------
    # Machines
    # maker: 加工木头，制作成琴身
    def maker(self):
        while True:
            yield self.woodCon.get(2)
            process_time = random.gauss(1, 0.2)
            yield self.env.timeout(process_time)
            yield self.prePaintCon.put(1)
    # painter: 为琴身涂漆
    def painter(self):
        while True:
            yield self.prePaintCon.get(1)
            process_time = random.gauss(4, 1)
            yield self.env.timeout(process_time)
            yield self.postPaintCon.put(1)
    # assembler: 组装琴身、电子元件，制作成吉他
    def assembler(self):
        while True:
            yield self.postPaintCon.get(1)
            yield self.elecCon.get(1)
            process_time = 1
            yield self.env.timeout(process_time)
            yield self.guitarCon.put(1)  
    # -----------------------------------------------------
    # Machine Generator: 生成多个 parallel machines
    def makerGen(self): # maker Generator
        for i in range(num_maker):
            yield self.env.process(self.maker())
    def painterGen(self): # painter Generator
        for i in range(num_painter):
            yield self.env.process(self.painter())
    def assemblerGen(self): # assembler Generator
        for i in range(num_assembler):
            yield self.env.process(self.assembler())
    # -----------------------------------------------------
    # 定义库存报警
    def wood_stock_control(self):
        yield self.env.timeout(0)
        while True:
            if self.woodCon.level <= wood_critial_stock:
                # 触发警报
                print('Wood stock bellow critical level ({0}) at time {1}'.\
                    format(self.woodCon.level, int(self.env.now)))
                # 联系供应商，购买 300 个木材
                print('Calling wood supplier...')
                yield self.env.timeout(wood_order_leadTime)
                print('Wood supplier arrives at time {0}'.format(int(self.env.now)))
                yield self.woodCon.put(wood_order_amount)
                print('New wood stock is {0}'.format(self.woodCon.level))
                print('------------------------------------------')
                # 进货一次之后，至少再等 8 个时间单位才能重新检查库存
                yield self.env.timeout(8)
            else:
                # 如果没有触发警报，就每隔 1 个时间单位检查一次库存
                yield self.env.timeout(1)
    
    def elec_stock_control(self):
        yield self.env.timeout(0)
        while True:
            if self.elecCon.level <= elec_critial_stock:
                print('Elec stock bellow critical level ({0}) at time {1}'.\
                    format(self.elecCon.level, int(self.env.now)))
                print('Calling elec supplier...')
                yield self.env.timeout(16)
                print('Elec supplier arrives at time {0}'.format(int(self.env.now)))
                yield self.elecCon.put(50)
                print('New elec stock is {0}'.format(self.elecCon.level))
                print('------------------------------------------')
                yield self.env.timeout(8)
            else:
                yield self.env.timeout(1)

    def guitar_stock_control(self):
        # 声明一个全局变量，来记录生产的吉他总数
        global guitars_made
        yield self.env.timeout(0)
        while True:
            if self.guitarCon.level >= 50:
                print('Guitar Containor stock is {0}, calling store to pick guitars at time {1}'.format(self.guitarCon.level, int(env.now)))
                yield env.timeout(4)
                print('Store picking {0} guitars at day time {1}'.format(self.guitarCon.level, int(env.now)))
                guitars_made += self.guitarCon.level
                yield self.guitarCon.get(self.guitarCon.level)
                print('----------------------------------')
                yield env.timeout(8)
            else:
                yield env.timeout(1)

# 创建环境、工厂对象
env = simpy.Environment()
factory = Guitar_Factory(env)
# Add machines
env.process(factory.makerGen())
env.process(factory.painterGen())
env.process(factory.assemblerGen())
# Add alarm and replenishment
env.process(factory.wood_stock_control())
env.process(factory.elec_stock_control())
# Simulate to time 500
env.run(until = 500)

print(f'%d products are produced!' % guitars_made)
```

# SimPy + Tkinter

使用 Tkinter 实现一个简单的 GUI，用于控制 SimPy 模拟的过程以及实现流程的可视化。参考: https://towardsdatascience.com/simulating-real-life-events-in-python-with-simpy-619ffcdbf81f

## .1 使用 Threading 避免 GUI 卡死

当 simulation 本身比较复杂时，可以使用 threading.Thread 为 GUI 创建一个独立的线程，减少卡顿

```python
def tkinterGUI_main(name):
    root = tk.Tk()
    root.title(name)
    root.geometry('800x600')
    root.mainloop()

GUI = threading.Thread(target=tkinterGUI_main, args=('SimPy_GUI'))
GUI.start()
env.run(until = 500)
```

## .2 SimPy + Tkinter.Toplevel

我们往往会希望在打开一个窗口时开始一个进程 `env.process()`，并且在关闭这个窗口时结束这个进程，从而避免资源浪费。这部分的内容详见 [python-lib-tkinter#Toplvel#Toplevel + Tkinter]()