
from flask import Flask, request

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def index():
    # # city = request.form.get('city')
    # sheng = request.form.get('sheng')
    # country = request.form.get('country')
    # # city = request.args.get('city')
    # city_list = request.form.getlist('city')
    # print(request.data)
    # return '%s %s %s' % (country, sheng, city_list)


    data = request.data
    print(data)
    print(type(data))
    a = data.decode('ascii')
    print(a)
    print('type--a',type(a))
    print('-------------')
    b =eval(a)
    print('type--b',type(b))

    print(b)
    return b.get('country')




if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)






