def set_func(foo):
    print('++++++++++++')

    def call_func():
        print('===权限验证===')
        foo()
        print('qqqqqqqqqqqqqq')
    return call_func


@set_func
def foo():
    print('======foo======')

foo()
