---
layout: wiki
title: Matlab-drawing
categories: Programming Language
description: 
keywords: [Matlab]
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
分成 $r\times c$ 个子窗口，$p$ 为子窗口排位(自左向右，自上而下)
```matlab
subplot(r, c, p) 
```

## 1.3 图片保存
将当前窗口显示的图片保存至 'image/i.jpg'
```matlab
print(gcf, '-djpeg', sprintf('image/%d.jpg',i))  
```

# 2 二维绘图

```matlab
plot(x, y, 'color_point_linestyle', 'linewidth', 2, 'markersize', 12);
```
'color_point_linestyle' = 线型 + 线色 + 数据点 (例如 `'--r*'`)
- 线型(-, -., --, : \)
- 线色(r-red, g-green, b-blue, w-white, k-black，i-invisible，y-yellow)
- 数据点(., o, x, +, *, S, H, D, V, ^)

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

## 2.3 等高线地图
```matlab
coun
```

# 3 三维绘图
## 3.1 三维条形图
```matlab
Z = [1, 1, 2, 3; 
     2, 2, 4, 6; 
     3, 3, 6, 8];
bar3(Z)
```

$z_{ij}=n$ 的绘制效果：<br> 在 x-y 坐标系下的 $(i,j)$ 位置绘制一个高 $n$ 的长方柱。例如：

<center>
    <img src="https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2021-02/202102011131.jpg" style="zoom:70%"> <br>
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
X = 1:0.3:100;
Z = sin(X) + cos(X)';

x = X + zeros(length(X), 1);
x = x(:);
y = x(randperm(length(x)));
z = Z(:);

s  = ones(length(z), 1) * 3;
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
    <img src="https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2021-02/202102021443.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 3-2：三维散点图</div>
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
    <img src="https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2021-02/202102031601.gif" style="zoom:50%"> <br>
    <div style="color: #999;">图 4-1：示例：gif 动图</div>
</center><br>
### 4.1.2 将现有的图片制作成 gif
令用于生成 gif 的图片集包含 10 张名为 'image1.jpg' ... 'image10.jpg' 的图片（matlab 图片保存详见 section 1.3）
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


