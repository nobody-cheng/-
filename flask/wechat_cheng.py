# coding:utf-8
from flask import Flask, request, abort
import hashlib

WECHAT_TOKEN = 'zhangcheng'

app = Flask(__name__)


@app.route('/wechat8012')
def wechat():
    # 接收微信服务器发送的参数
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    # 校验参数
    if not all([signature, timestamp, nonce, echostr]):
        abort(400)
    # 进行签名
    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    # 拼接字符串
    tmp_str = ''.join(li)
    # 进行sha1加密
    sign = hashlib.sha1(tmp_str).hexdigest()
    # 将自己计算签名与请求的签名参数进行对比,若相同,则请求来自微信服务器
    if signature != sign:
        abort(403)
    else:
        return echostr


if __name__ == '__main__':
    app.run(port=8012, debug=True)
