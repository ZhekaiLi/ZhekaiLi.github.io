---
layout: wiki
title: Matlab
categories: Programming Language
description: 
keywords: [Matlab]
---

# 1 Drawing
**2D 绘图**
```matlab
plot(x, y, '--r*', 'linewidth', 2, 'markersize', 12);
```
## 1.1 常用命令
```matlab
hold on;  # 持续绘图
hold off; 
```
**标注**
```matlab
xlabel(''); 
ylabel('');
title(''); 
axis([xmin, xmax, ymin, ymax]);
```
```matlab
text(x, y, '')  # 图内文字
# 在指定位置插入文字
# 这个命令会在图片窗口显示后生成一个会随鼠标移动的十字光标
# 需要移动光标来指定插入文字的位置
gtext('');
```
**更改坐标轴**
```
```

