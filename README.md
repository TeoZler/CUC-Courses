# CUC_Courses

CUC的抢课脚本

## 使用教程

1. 打开选课网站，登录后打开`f12`-`网络`，选择自己想要的课，点击红框处

![](https://s2.loli.net/2022/06/30/nCGk5483IuKd2QB.png)

1. 在`标头`-`请求标头`中复制`Cookie`和`token`，分别填入xsxk.py中的`cookie`和`url_totens`。（此步骤只用执行一次）

​	复制`荷载`-`表单数据`-`查看源代码`中的数据，填入xsxk.py中的`data`（每个课都需要复制一次）

执行`python xsxk.py`