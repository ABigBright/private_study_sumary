class TestA(object):
    mm = 'hello TestA'

    def __new__(self):
        return "hehe"

print(TestA.mm)
print(type(TestA()))