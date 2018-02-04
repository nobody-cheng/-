# @property

class Person(object):
    def __init__(self, first_name, last_name):
        """构造"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """返回"""
        return '%s & %s' % (self.first_name, self.last_name)


p = Person('A', 'B')
print(p.full_name)
print(p.first_name)
print(p.last_name)
print(p.full_name)