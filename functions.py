# about returning a function inside a function
import threading;
# late callback / Asyc callback
def functiona():
    def functionb():
        print("python allows inner function");
        def functionc():
            print("Inside function cc")
        return functionc;
    return functionb;

a = functiona;
print(a()()())

#  generators   is knowns stateful methods
def test():
    print("step1");
    yield 10;

    print("step2")
    yield 50

    print("step3")
    yield 100
a = test();
val1 = a.__next__();

a = test();

for x in a:
    print(x)


a = lambda x,y: (x+y);

print(a(1,2))






