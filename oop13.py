class A:
    def introduce(self):
        return "Class A"


class B(A):
    def introduce(self):
        return "Class B"

class C(A):
    def introduce(self):
        return "Class C"

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

print(a.introduce())
print(b.introduce())
print(c.introduce())
print(d.introduce())

print(D.mro())