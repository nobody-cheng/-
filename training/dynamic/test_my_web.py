import time
import re
from pymysql import *
import urllib.parse

g_templates_root = './templates'
# g_path_func = {
#     "/index.py": index,
#     "/center.py": center
# }
g_path_func = {}
# 假设已经有了一个装饰器  当定义index 方法的时候 就能够自动完成 "/index.py" 和 index方法的对应
# 有参数的装饰器


def router(pattern):
    def set_func(foo):
        # 完成一种映射
        # key:  正则表达式的规则
        # value: 函数的名称
        print('开始装饰 %s', foo)
        g_path_func[pattern] = foo

        def call_func():
            print('~~~~~~~~~~call_func~~~~~~~~~~~~')
            foo()
        return call_func
    return set_func


@router(r"/index\.html")    # router("/index.py")  --> set_func  装饰的过程如下 index = set_func(index)
def index(pattern, file_path):
    # 获取到模板文件
    # 将 .py 换成 .html
    # file_path = file_path.replace(".py" ,".html")
    try:
        f = open(g_templates_root + file_path, encoding="utf-8")
    except Exception as ret:
        return str(ret)
    else:
        content = f.read()
        f.close()


        # 从mysql 中获取数据  # 填充到模板

        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cur = db.cursor()
        sql = "select * from info"
        cur.execute(sql)
        ret = cur.fetchall()   # 元组


        html_template = """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>
                            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                        </td>
                    </tr>"""
        html = ""
        for item in ret:
            html += html_template % (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[1])

        content = re.sub(r"\{%content%\}", html, content)
        cur.close()
        db.close()

        return content


@router(r'/center\.html')
def center(pattern, file_path):
    try:
        f = open(g_templates_root + file_path, encoding='utf-8')
    except Exception as result:
        return str(result)
    else:
        content = f.read()
        f.close()

        db = connect(host='localhost',
                     port=3306,
                     database='stock_db',
                     user='root',
                     password='mysql',
                     charset='utf8')
        cur = db.cursor()
        sql = "select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info " \
              "from info as i inner join focus as f on i.id = f.info_id"
        cur.execute(sql)
        ret = cur.fetchall()

        html_temlate = """<tr>
                               <td>%s</td>
                               <td>%s</td>
                               <td>%s</td>
                               <td>%s</td>
                               <td>%s</td>
                               <td>%s</td>
                               <td>%s</td>
                               <td>
                                   <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                               </td>
                               <td>
                                   <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                               </td>
                           </tr>"""

        html = ""
        for item in ret:
            html += html_temlate % (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[0], item[0])
        content = re.sub(r'\{%content%\}', html, content)
        cur.close()
        db.close()
        return content


# /add/000540.html
# /add/000541.html
# /add/000542.html
# 一个文件路径 对应一个方法
@router(r'/add/(\d*)\.html')
def add(pattern, file_path):
    print(pattern, file_path)
    # 股票---》添加股票代码 focus
    ret = re.match(pattern, file_path)
    stock_code = ret.group(1)
    print('--------添加股票代码------', stock_code)

    # 根据股票代码 找到info_id 储存到focus表中
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()

    # 标量子查询
    sql = 'select * from focus where info_id = (select id from info where code = %s)'
    cur.execute(sql, [stock_code])
    ret = cur.fetchone()
    if ret:
        # 找到了结果
        cur.close()
        db.close()
        return '请不要重复关注'
    sql = 'insert into focus (info_id) select id from info where code = %s'
    cur.execute(sql, [stock_code])
    db.commit()
    cur.close()
    db.close()
    return '关注成功'


# /update/300268.html
@router(r'/update/(\d*)\.html')
def update(pattern, file_path):
    print(pattern, file_path)
    ret = re.match(pattern, file_path)
    stock_code = ret.group(1)
    print(stock_code)

    # 1.读取模板文件
    try:
        f = open(g_templates_root + '/update.html', encoding='utf-8')
    except Exception as result:
        return str(result)
    else:
        content = f.read()
        f.close()
        # 2. 从mysql 中查询数据 通过股票代码 获取 股票名字 和备注信息
        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cur = db.cursor()

        sql = 'select short,id from info where code = %s'
        cur.execute(sql, [stock_code])
        ret = cur.fetchone()
        short = ret[0]
        id = ret[1]

        sql = 'select note_info from focus where info_id = %s'
        cur.execute(sql, [id])
        ret = cur.fetchone()
        note_info = ret[0]

        content = re.sub(r'\{%code%\}', short, content)
        content = re.sub(r'\{%note_info%\}', note_info, content)
        cur.close()
        db.close()
        return content


# /update/%E5%8D%97%E9%80%9A%E9%94%BB%E5%8E%8B/haha.html
@router(r'/update/(.*)/(.*)\.html')
def update_note_info(pattern, file_path):
    print('=====pattern==========file_path=======', (pattern, file_path))
    ret = re.match(pattern, file_path)
    stock_name = ret.group(1)
    # unquote-----》编码之后字符串，解码
    # quote----------->对某个字符串编码
    stock_name = urllib.parse.unquote(stock_name)
    print('*******stock_name*********', stock_name)
    note_info = ret.group(2)
    note_info = urllib.parse.unquote(note_info)

    # 从mysql 中查询数据 通过股票代码 获取 股票名字 和备注信息
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()

    # 更新
    sql = "update focus set note_info = %s where info_id = (select id from info where short = %s)"
    cur.execute(sql, [note_info, stock_name])

    # 返回数据
    db.commit()
    cur.close()
    db.close()
    return "修改成功"


# /del/000056.html
@router(r'/del/(.*)\.html')
def delete(pattern, file_path):
    ret = re.match(pattern, file_path)
    stock_code = ret.group(1)
    print(stock_code)
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()
    sql = "delete from focus where info_id = (select id from info where code = %s)"
    cur.execute(sql, [stock_code])

    # 数据更新 必须 commit
    db.commit()
    return "取消关注成功"


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    # 调用函数 在web_server定义
    start_response(status, response_headers)
    file_path = environ['PATH_INFO']
    # index.html
    # g_path_func = {r"/index\.html": index,
    #                     r"/center\.html": center,
    #                     r"/add/(\d*)\.html": add
    #                     }
    try:
        # /add/000540.html
        # 遍历字典 把字典的键值信息都获取到
        for pattern, func in g_path_func.items():
            # 根据正则表达式 在去匹配file_path
            ret = re.match(pattern, file_path)
            if ret:
                # 满足膜一个正则表达式 调用func
                return func(pattern, file_path)
                # 根据正则表达式的规则 找到了对应的路径之后 就不需要在找了
        else:
            return '没有对应的链接'

    except Exception as result:
        return str(result)
