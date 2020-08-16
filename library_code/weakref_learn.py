import gc
import weakref


class C:
    def method(self):
        print("method called!")


c = C()
r = weakref.ref(c.method)
r()
r = weakref.WeakMethod(c.method)
print(r())  # <bound method C.method of <__main__.C object at 0x106d425b0>>

r()()  # method called!

del c
gc.collect()

print(r())  # None



