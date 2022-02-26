from dataclasses import dataclass

@dataclass
class F:
    a: int
    b: str

    # def __hash__(self): return (self.a,self.b).__hash__()

    def __eq__(self, other): return self.a == other.a and self.b == other.b

f1 = F(1, 'a')
f2 = F(1, 'a')

s = set()
s.add(f1)
s.add(f2)

print(s)

