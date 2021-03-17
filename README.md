# Jd_Seckill

## 主要功能

- 登陆京东商城（[www.jd.com](http://www.jd.com/)）
  - 用京东APP扫码给出的二维码
- 每天自动预约并抢购茅台，无需中止

## 运行环境

- [Python 3](https://www.python.org/)

## 第三方库

- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令  
`pip install -r requirements.txt`
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速
`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`

## 使用教程  
#### 1. 推荐Chrome浏览器
#### 2. 网页扫码登录，或者账号密码登录
#### 3. 填写config.ini配置信息 
(1)`eid`和`fp`找个普通商品随便下单,然后抓包就能看到,这两个值可以填固定的 
> 随便找一个商品下单，然后进入结算页面，打开浏览器的调试窗口，切换到控制台Tab页，在控制台中输入变量`_JdTdudfp`，即可从输出的Json中获取`eid`和`fp`。  
> 不会的话参考原作者的issue https://github.com/zhou-xiaojun/jd_mask/issues/22

(2)`sku_id`,`DEFAULT_USER_AGENT` 
> `sku_id`已经按照茅台的填好。
> `DEFAULT_USER_AGENT` 可以用默认的。谷歌浏览器也可以浏览器地址栏中输入about:version 查看`USER_AGENT`替换

(3)配置一下时间
> 现在不强制要求同步最新时间了，程序会自动同步京东时间
>> 但要是电脑时间快慢了好几个小时，最好还是同步一下吧

以上都是必须的.
> tips：
> 在程序开始运行后，会检测本地时间与京东服务器时间，输出的差值为本地时间-京东服务器时间，即-50为本地时间比京东服务器时间慢50ms。
> 本代码的执行的抢购时间以本地电脑/服务器时间为准

(4)修改抢购瓶数
> 代码中默认抢购瓶数为2，且无法在配置文件中修改
> 如果一个月内抢购过一瓶，最好修改抢购瓶数为1 
> 具体修改为：在`jd_spider_requests.py`文件中搜索`self.seckill_num = 2`，将`2`改为`1`

#### 4.运行main.py 

#### 5.抢购结果确认 
抢购是否成功通常在程序开始的一分钟内可见分晓！  
搜索日志，出现“抢购成功，订单号xxxxx"，代表成功抢到了，务必半小时内支付订单！程序暂时不支持自动停止，需要手动STOP！  
若两分钟还未抢购成功，基本上就是没抢到！程序暂时不支持自动停止，需要手动STOP！  


