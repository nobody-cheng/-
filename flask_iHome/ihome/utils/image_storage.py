# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'sCi0XEDdRe2pmiwvDQedYI4V6UHjJzQz3rDImSzf'
secret_key = 'ae1opPR11ATMxNeXErJDTvfexhm281WYhDtbp7PX'


def storage(file_data):
    """上传文件到七牛服务器"""
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'ihome'

    # # 上传到七牛后保存的文件名
    # key = 'my-python-logo.png'

    # 生成上传 Token，可以指定过期时间等
    # token = q.upload_token(bucket_name, key, 3600)
    token = q.upload_token(bucket_name, None, 3600)

    # # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'

    ret, info = put_data(token, None, file_data)
    print ('=======', ret)
    print ('*******', info)
    if info.status_code == 200:
        # 头像上传成功
        # ('====ret===', {u'hash': u'Fu_bFrcTMjUwyNHfdpHf_AITBO0q', u'key': u'Fu_bFrcTMjUwyNHfdpHf_AITBO0q'})
        return ret.get('key')
    else:
        raise Exception('头像上传七牛服务器失败')


if __name__ == '__main__':
    with open('./32.jpg', 'rb') as f:
        file_data = f.read()
        storage(file_data)
