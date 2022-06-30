# CUC_Courses

CUC的抢课脚本

## 使用教程

1. clone此项目。`git clone https://github.com/TeoZler/CUC-Courses`
2. 打开选课网站，登录后打开`f12`-`网络`，选择自己想要的课，点击红框处名称为volunteer.do的项。![](https://s2.loli.net/2022/06/30/nCGk5483IuKd2QB.png)
3. 在`标头`-`请求标头`中复制`Cookie`和`token`，分别填入xsxk.py中的`cookie`和`url_totens`。（此步骤只用执行一次）
4. 复制`荷载`-`表单数据`-`查看源代码`中的数据，填入xsxk.py中的`data`。（每个课都需要复制一次）
5. 执行`python xsxk.py`

## 存在的问题

`Cookie`和`token`都有时效限制，使用前最好重新获取一次。
