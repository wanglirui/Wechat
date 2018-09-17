
import itchat
import json
import requests
import codecs
KEY = ' 你申请的key'
sex_dict = {}
sex_dict['0'] = "其他"
sex_dict['1'] = "男"
sex_dict['2'] = "女"

def get_response(msg):
 apiUrl = 'http://www.tuling123.com/openapi/api'
 data = {
  'key' : KEY,
  'info' : msg,
  'userid' : '11112kkk',
 }
 r = requests.post(apiUrl, data=data).json()
 print(r)
 return r.get('text')
#下载好友头像
def download_images(frined_list):
    image_dir = "./images/"
    num = 1
    for friend in frined_list:
        image_name = str(num)+'.jpg'
        num+=1
        img = itchat.get_head_img(userName=friend["UserName"])
        with open(image_dir+image_name, 'wb') as file:
            file.write(img)

def save_data(frined_list):
    out_file_name = "./data/friends.json"
    with codecs.open(out_file_name, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(frined_list,ensure_ascii=False))

# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     NickName = msg['User']['NickName']
#     user = itchat.search_friends(name=NickName)[0]
#     text = msg['Text']
#
#     if text in message_dict.keys():
#         user.send(message_dict[text])
#     else:
#         user.send(u"你好啊%s,我目前还不支持这个功能"%NickName)

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
 defaultReply = 'I received: ' + msg['Text']
 reply = get_response(msg['Text'])
 user = itchat.search_friends(name=u'还没想好')[0]
 user.send(reply)
 print(reply)
 # return reply
if __name__ == '__main__':
    itchat.auto_login()
    
    friends = itchat.get_friends(update=True)[0:]#获取好友信息
    friends_list = []

    for friend in friends:
        item = {}
        item['NickName'] = friend['NickName']
        item['HeadImgUrl'] = friend['HeadImgUrl']
        item['Sex'] = sex_dict[str(friend['Sex'])]
        item['Province'] = friend['Province']
        item['Signature'] = friend['Signature']
        item['UserName'] = friend['UserName']

        friends_list.append(item)
        print(item)
    #
    save_data(friends_list)
    download_images(friends_list)

    
    user = itchat.search_friends(name=u'还没想好')[0]
    user.send(u'hello,这是一条来自机器人的消息')
    itchat.run()
