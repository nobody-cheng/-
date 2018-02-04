class Fib(object):
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num1
        if self.current < self.n:
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num 
        else:
            raise StopIteration

if __name__ == '__main__':
    fib = Fib(10)
    for num in fib:
        print(num)
