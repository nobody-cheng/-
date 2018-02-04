def make_bold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'
    return wrapped


def make_italic(fn):
    def wrapped():
        return '<A>' + fn() + '</A>'
    return wrapped


@make_bold
@make_italic
def test3():
    return 'hello world python'


@make_bold
def test1():
    return 'hello world'


@make_italic
def test2():
    return 'hello python'
ret3 = test3()
print(ret3)

ret1 = test1()
print(ret1)


ret2 = test2()
print(ret2)


