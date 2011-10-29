print 'hello world'
print 'the quick brown fox jumps over the lazy dog'

import sys

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Name: " + self.name
    
class Bar(Foo):
    def __init__(self, name, age):
        super(Bar, self).__init__(name)
        self.age = age
    def __str__(self):
        return super(Bar, self).__str__() + ", Age: " + self.age.__str__()

class Baz(Bar):
    def __init__(self, name, age, sex):
        super(Baz, self).__init__(name, age)
        self.sex = sex
    def __str__(self):
        return super(Baz, self).__str__() + ", Sex: " + self.sex.__str__()
    
def run():
    foo = Foo("Alice")
    bar = Bar("Bob", 30)
    baz = Baz("Charlie", 21, "Male")
    print foo
    print bar
    print baz
    

if __name__ == '__main__':
    run()