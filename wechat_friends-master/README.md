
# 微信机器人自动回复

## 功能说明：自动回复好友并统计好友信息
#### 1：统计好友的性别
![python](https://github.com/wanglirui/Wechat/blob/master/wechat_friends-master/source/%E4%B8%8B%E8%BD%BD%20(4).png)
#### 2：统计好友的地域分布，并且可视化在地图上展示
![python](https://github.com/wanglirui/Wechat/blob/master/wechat_friends-master/source/%E4%B8%8B%E8%BD%BD.png)

![python](https://github.com/wanglirui/Wechat/blob/master/wechat_friends-master/source/%E4%B8%8B%E8%BD%BD%20(1).png)
#### 3：将好友的昵称做成词云
因为这个信息比较私人，这里就不展示
#### 4：统计好友个性签名中的高频词汇
![python](https://github.com/wanglirui/Wechat/blob/master/wechat_friends-master/source/%E4%B8%8B%E8%BD%BD%20(3).png)
#### 5：将所有好友的头像合并成一张大图
因为这个信息比较私人，这里就不展示
#### 6：微信自动发送与回复消息


## 依赖
本程序使用python3，请在python3环境下运行
#### Python 3
- PIL: pip3 install pillow
- pyecharts：pip3 install pyecharts
- pip3 install itchat
- pip3 install jieba

地图数据包：  
pip3 install echarts-china-provinces-pypkg  
pip3 install echarts-countries-pypkg

## 运行
#### 获取用户信息
需要将get_user_info.py 的好友名字改成需要发送信息的好友昵称，为了显得智能一点，我申请了一个图灵机器人，http://www.tuling123.com/ ，申请成功后找到对应的KEY填入代码里。
  
python3 get_user_info.py
执行后会在data目录下生成friends.json
会在images目录下存放所有好友的头像
#### 统计用户信息
python3 analyse.py
会在analyse文件夹下生产合成后的图片以及可视化的文件
