# coding:utf-8

from flask import Flask, request, abort, render_template
import hashlib
import xmltodict
import time
import urllib2
import json

#  微信的token令牌
WECHAT_TOKEN = 'zhangcheng'
# 登陆测试平台后　"自己的appid"
WECHAT_APPID = 'wxff319cfbda458452'
# 登陆测试平台后 自己的appsecret
WECHAT_APPSECRET = '7177b1f43ed07c4fc808b8952a98714d'

app = Flask(__name__)


@app.route('/wechat8012', methods=['GET', 'POST'])
def wechat():
    # 接收微信服务器发送的参数
    """
    signature 微信加密签名，其结合了开发者填写的ｔｏｋｅｎ参数
    和请求中的timestamp,nonce参数
    timestamp 时间戳
    nonce 随机数
    echostr 随机字符串
    将token、timestamp、nonce三个参数进行字典序排序,拼接成一个字符串进行sha1加密
    开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    """
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")

    # 校验参数
    if not all([signature, timestamp, nonce]):
        abort(401)
    # 进行签名
    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    # 拼接字符串
    tmp_str = ''.join(li)
    # 进行sha1加密
    sign = hashlib.sha1(tmp_str).hexdigest()
    # 将自己计算签名和请求的签名参数对比，相同则请求来至微信服务器
    if signature != sign:
        abort(402)
    else:
        # 表示是微信发送的请求
        if request.method == 'GET':
            # 表示第一次接入微信服务器的验证
            echostr = request.args.get('echostr')
            if not echostr:
                abort(403)
            return echostr
        elif request.method == 'POST':
            # 表示微信服务器转发消息过来
            xml_str = request.data
            if not xml_str:
                abort(404)

            # 对ｘｍｌ字符串进行解析
            xml_dict = xmltodict.parse(xml_str)
            xml_dict = xml_dict.get('xml')

            msg_type = xml_dict.get('MsgType')

            if msg_type == 'text':
                # 表示发送过来的是文本，构造返回值，经由微信服务器回复给用户
                # FromUserName开发者微信号
                # ToUserName 接收方帐号
                resp_dict = {
                    'xml': {
                        "ToUserName": xml_dict.get("FromUserName"),
                        "FromUserName": xml_dict.get("ToUserName"),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": xml_dict.get("Content")
                    }
                }
            # elif msg_type == 'voice':
            #     resp_dict = {
            #         'xml': {
            #             "ToUserName": xml_dict.get("FromUserName"),
            #             "FromUserName": xml_dict.get("ToUserName"),
            #             "CreateTime": int(time.time()),
            #             "MsgType": "voice",
            #             'MediaId': xml_dict.get("MediaId"),
            #             'Format': xml_dict.get("Format"),
            #             'Recognition': xml_dict.get("Recognition"),
            #             'MsgId': xml_dict.get("MsgId"),
            #         }
            #     }
            else:
                resp_dict = {
                    "xml": {
                        "ToUserName": xml_dict.get("FromUserName"),
                        "FromUserName": xml_dict.get("ToUserName"),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": "biu biu biu biu "
                    }
                }

            # 将字典转换为xml字符串
            resp_xml_str = xmltodict.unparse(resp_dict)
            # 返回消息数据给微信服务器

            return resp_xml_str


# www.itcastcpp.cn/wechat8012/index_wechat
@app.route('/wechat8012/index_wechat')
def index_wechat():
    # 让用户通过微信访问网页页面视图
    # 从微信服务器中拿去用户的资料数据
    # １．拿去code参数
    code = request.args.get("code")

    if not code:
        return u'没有获取到code 参数'

    # 2.向微信服务器发送ｈｔｔｐ请求，获取access_token
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" \
          % (WECHAT_APPID, WECHAT_APPSECRET, code)
    # 使用urllib2的urlopen方法发送请求
    # 如果只传网址url参数，则默认使用http的get请求方式, 返回响应对象
    response = urllib2.urlopen(url)
    # 获取响应体数据，微信返回的json数据
    json_str = response.read()
    resp_dict = json.loads(json_str)

    # 提取access_token
    if 'errcode' in resp_dict:
        return u'获取access_token失败'
    access_token = resp_dict.get('access_token')
    open_id = resp_dict.get('openid')  # 用户编号

    # 3. 向微信服务器发送http请求，获取用户的资料数据
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" \
          % (access_token, open_id)

    response = urllib2.urlopen(url)

    # 读取微信传回的json的响应体数据
    user_json_str = response.read()
    user_dict_data = json.loads(user_json_str)

    if 'errcode' in user_dict_data:
        return u'获取用户信息失败'
    else:
        # 将用户的资料填充到页面中
        return render_template('index_wechat.html', user=user_dict_data)


"""正确时返回的JSON数据包如下：

{    "openid":" OPENID",

 " nickname": NICKNAME,

 "sex":"1",

 "province":"PROVINCE"

 "city":"CITY",

 "country":"COUNTRY",

 "headimgurl":    "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ

4eMsv84eavHiaiceqxibJxCfHe/46",

"privilege":[ "PRIVILEGE1" "PRIVILEGE2"     ],

 "unionid": "o6_bmasdasdsad6_2sgVt7hMZOPfL"

} """

if __name__ == '__main__':
    app.run(debug=True, port=8012)
