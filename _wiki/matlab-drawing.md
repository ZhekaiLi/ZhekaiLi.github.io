---
layout: wiki
title: Drawing
cate1: Matlab
cate2:
description: 
keywords: Matlab
mathjax: true
---

# 1 常用命令
```matlab
hold on;  % 持续绘图
hold off; 
```
## 1.1 标注
```matlab
xlabel(''); 
ylabel('');
title(''); 
axis([xmin, xmax, ymin, ymax]);
```
```matlab
text(x, y, '')  % 图内文字
% 在指定位置插入文字
% 这个命令会在图片窗口显示后生成一个会随鼠标移动的十字光标
% 需要移动光标来指定插入文字的位置
gtext('');
```
## 1.2 绘制多个子图
分成 `r*c` 个子窗口，`p` 为子窗口排位(自左向右，自上而下)
```matlab
subplot(r, c, p) 
```

## 1.3 图片保存
将当前窗口显示的图片保存至 `'image/i.jpg'`
```matlab
print(gcf, '-djpeg', sprintf('image/%d.jpg',i))  
```

## 1.4 更改图像色调
在绘图命令后输入以下代码：
```matlab
colormap(hot);
```
更多色调模式以及自定义方式请参照[官网说明](https://ww2.mathworks.cn/help/matlab/ref/colormap.html)

## 1.5 坐标轴控制
```matlab
axis off;  % 显示绘图而不显示坐标区背景
axis tight;  % 将坐标轴范围设置为等于数据范围
axis ij;  % 反转坐标系，这样 y 的值按从上到下的顺序逐渐增加
axis manual;  % 将范围设置为手动，从而保留当前的坐标轴范围（不会随着之后
              % 图像的添加而变化）
```


# 2. 二维绘图
```matlab
plot(x, y, 'color_point_linestyle', 'linewidth', 2, 'markersize', 12);
```
`'color_point_linestyle'` = 线型 + 线色 + 数据点 (例如 `'--r*'`)
- 线型 (-, -., --, : \)
- 线色 (r-red, g-green, b-blue, w-white, k-black，i-invisible，y-yellow)
- 数据点 (., o, x, +, *, S, H, D, V, ^)

## 2.1 极坐标绘图
```matlab
x = 0:0.1:2*pi; 
r = cos(2*x); 

polar(x, r)
```

## 2.2 函数绘图
`fplot(fun, lims)` 绘制由字符串 `fun` 指定函数名的函数在 $x$ 轴区间为 `lims=[xmin, xmax]` 的函数图。例如：
$$f(x)=\begin{cases}
x + 1,\;\;x<1\\
1 +\frac{1}{x},\;\; x\geq 1
\end{cases}$$

## 2.3 等高线图
```matlab
[M, c] = contourf(X, Y, Z, 20)
```
- `X, Y` 都是二维矩阵，储存点的横纵坐标（一般用 `meshgrid()` 生成）
- `Z` 为二维矩阵，储存点的高度
- `20` 表示将等高线地图强制划分为 20 个层级
- `M` 为等高线矩阵
- `c` 为等高线对象，可以对其进行属性设置（线形、线色），例如：<br> `c.EdgeColor='none'` 不显示区分线

示例：
```matlab
[X, Y] = meshgrid(1:20, 1:20);
Z = Y - X;

[M, c] = contourf(X, Y, Z, 20);
c.EdgeColor = 'none';
```
<center>
    <img src="/images/2021-02/202102031635.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 2-1：等高线图</div>
</center><br>
### 2.3.1 梯度与箭头绘制
> **生成梯度**

```matlab
[DX, DY] = gradient(Z, dx, dy)
```
- `Z` 为二维矩阵，储存点的高度
- `dx, dy` 为数字，表示箭头绘制的间隔（越大表示箭头越稀疏）

> **绘制箭头**

```matlab
quiver(X, Y, DX, DY)  % 这个没啥好解释的
```
示例（矩阵 `X, Y, Z` 源于 **section 2.3**）
```matlab
[M, c] = contourf(X, Y, Z, 20);
c.EdgeColor = 'none'; hold on;

[DX,DY] = gradient(Z,1,0.5);
quiver(X, Y, -DX, -DY);
```
<center>
    <img src="/images/2021-02/202102041648.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 2-2：带箭头的等高线图</div>
</center><br>

## 2.4 柱状图

# 3. 三维绘图
## 3.1 三维条形图
```matlab
Z = [1, 1, 2, 3; 
     2, 2, 4, 6; 
     3, 3, 6, 8];
bar3(Z)
```

`z_{ij}=n` 的绘制效果：<br> 在 x-y 坐标系下的 `(i,j)` 位置绘制一个高 `n` 的长方柱。例如：

<center>
    <img src="/images/2021-02/202102011131.jpg" style="zoom:70%"> <br>
    <div style="color: #999;">图 3-1：三维条形图</div>
</center><br>

## 3.2 三维散点图
```matlab
scatter3(x, y, z, s, c);

% x, y, z 即三维空间坐标
% s 表示散点的大小
% c 表示散点的颜色
```
示例：
```matlab
[X, Y] = meshgrid(1:0.3:100, 1:0.3:100);
Z = sin(X) + cos(X)';

x = X(:); y = Y(:); z = Z(:);
s = ones(length(z), 1) * 3;

% 给点上色
c = [];
for i = 1:length(z)
    if z(i) > 1.5, c(i, :) = [1 0 0];
    elseif z(i) < 0.5, c(i, :) = [0 1 0];
    else, c(i, :) = [0 0 1];
    end   
end

scatter3(x, y, z, s, c)
```
<center>
    <img src="/images/2021-02/202102021443.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 3-2：三维散点图</div>
</center><br>

## 3.3 三维曲面图
```matlab
surf(X, Y, Z);
```
示例：
```matlab
[X, Y] = meshgrid(1:0.3:10, 1:0.3:10);
Z = sin(X) + cos(Y);

s = surf(X, Y, Z);
s.EdgeColor = 'none';
```
<center>
    <img src="/images/2021-02/202102041804.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 3-3：三维曲面图</div>
</center><br>

## 3.4 三维几何体
### 3.4.1 圆柱和圆台
```matlab
[X, Y, Z] = cylinder(r)
```
- `r` 表示圆台/ 圆柱半径的变化，可以是关于 `t` 的函数

示例：
```matlab
figure;
t = 0:0.1:1;

subplot(1, 2, 1);
[X, Y, Z] = cylinder(1.5);
surf(X, Y, Z); axis square;

subplot(1, 2, 2);
[X, Y, Z] = cylinder(2 - t);
surf(X, Y, Z); axis square;
```
<center>
    <img src="/images/2021-02/202002042037.jpg" style="zoom:70%"> <br>
    <div style="color: #999;">图 3-4：圆锥/ 圆台图 </div>
</center><br>



# 4 其他
## 4.1 制作 gif
### 4.1.1 画图的同时生成 gif
```matlab
p = scatter(randn, randn);
axis([-3, 3, -3, 3]); hold on;

% 将当前图像存储至变量 A, map
% getframe 表示获取当前图像
[A,map] = rgb2ind(frame2im(getframe),256);

% 将 A, map 存储为 'image.gif' 图像的第一帧
imwrite(A,map,'image.gif','LoopCount',65535,'DelayTime',0.1);

for i = 1:10
    p = scatter(randn, randn); hold on; 
    [A,map] = rgb2ind(frame2im(getframe),256);
    % 将新的 A, map 存储为新的一帧并添加至 'image.gif' 中
    imwrite(A,map,'image.gif','WriteMode','append','DelayTime',0.1);
    pause('on')
    pause(0.2)
end
```
效果图：
<center>
    <img src="/images/2021-02/202102031601.gif" style="zoom:50%"> <br>
    <div style="color: #999;">图 4-1：示例：gif 动图</div>
</center><br>
### 4.1.2 将现有的图片制作成 gif
令用于生成 gif 的图片集包含 10 张名为 `'image1.jpg'` ... `'image10.jpg'` 的图片（matlab 图片保存详见 section 1.3）
```matlab
for j=1:10
    % 获取图片
    I = imread(sprintf('image%d.jpg',i));
    [A,map] = rgb2ind(I,256);

    % 生成 gif 并保存
    if(i == 1)
        imwrite(A,map,'image.gif','DelayTime',0.1,'LoopCount',Inf);
    else
        imwrite(A,map,'image.gif','WriteMode','append','DelayTime',0.1);    
    end
end
```


