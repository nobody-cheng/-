from flask import Flask, request

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    file_obj = request.files.get('pic')
    if file_obj:
       f = open('./test.jpg','wb')
       data = file_obj.read()
       f.write(data)
       f.close()
       return '上传成功'
    else:
        return '未上传数据'

    # if file_obj is None:
    #     return '未上传数据'
    # f = open('./test.jpg', 'wb')
    # data = file_obj.read()
    # f.write(data)
    # f.close()
    # return '上传成功'


if __name__ == '__main__':
    app.run(debug=True)
