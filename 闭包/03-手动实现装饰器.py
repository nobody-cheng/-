def set_func(foo):
    def call_func():
        print('权限验证')
        foo()
    return call_func


def foo():
    print('======foo=====')

func = set_func(foo)
func()


