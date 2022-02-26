class F:
    a: int

    def __init__(self, a: int):
        self.a = a

    def __eq__(self, other):
        return self.a == other.a + 1

    def __add__(self, other):
        return F(self.a + other.a)


f1 = F(0)
f2 = F(10)
f3 = F(11)

print(f2 == f3)
f1.__add__(f2)
print(f1.a)
f1 += f2

print(f1.a)
