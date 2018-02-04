# def foo(k, b):
#     print('=======foo=======')
#
#     def foo_in(x):
#         print(k*x + b)
#
#     return foo_in
#
# ret = foo(2, 2)
# ret(2)
# ret(4)
# ret(6)


# def set_func(foo):
#     def call_func():
#         print('权限验证')
#         foo()
#     return call_func
#
#
# @set_func
# # 相当于foo = set_func(foo)
# def foo():
#     print('++++++++foo+++++++++++')
# foo()
# def set_func(foo):
#     def call_func1(*args, **kwargs):
#         print('权限验证')
#         print(args, kwargs)
#         foo(*args, **kwargs)
#     return call_func1
#
#
# @set_func
# def foo(*args, **kwargs):
#     print('++++++++++')
# foo(10, 20, a=22, b=33)