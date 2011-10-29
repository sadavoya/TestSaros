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

def run():
    foo = Foo("Jeff")
    bar = Bar("Drew", 39)
    print foo
    print bar
    

if __name__ == '__main__':
    run()