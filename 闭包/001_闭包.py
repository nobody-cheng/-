def test(num):
    def test_in(num_in):
        print('in test_in is', num_in)
        # return num + num_in

    return test_in

print(test)
ret = test(100)
print(ret)
print(ret(1))
print(ret(2))
print(ret(4))
print(ret(6))