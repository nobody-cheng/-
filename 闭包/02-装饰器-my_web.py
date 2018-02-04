import re
import time

g_templates_root = './templates'


g_path_func = {}


def router(path):
    def set_func(foo):
        # 完成一种映射，key:'/index.py',value:index函数的引用
        g_path_func[path] = foo

        def call_func():
            foo()
        return call_func
    return set_func


@router('/center.py')
def center(file_path):
    file_path = file_path.replace('.py', '.html')
    try:
        f = open(g_templates_root + file_path)
    except Exception as result:
        return str(result)
    else:
        content = f.read()
        f.close()
        data_from_mysql = '从mysql中查到了相应的数据'
        content = re.sub(r'\{content\}', data_from_mysql, content)
        print(content)
        return content


@router('/index.py')
def center(file_path):
    file_path = file_path.replace('.py', '.html')
    try:
        f = open(g_templates_root + file_path)
    except Exception as result:
        return str(result)
    else:
        content = f.read()
        f.close()
        data_from_mysql = '从mysql中查到了响应的数据'
        content = re.sub(r'\{content\}', data_from_mysql, content)
        return content


def app(environ, start_response):

    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_path = environ['PATH-INFO']
    try:
        return g_path_func[file_path](file_path)
    except Exception as result:
        return str(result)
