from dataclasses import dataclass


@dataclass
class F:
    a: int
    b: str

    def __lt__(self, other):
        return (self.a < other.a)

f1 = F(1, 'a')
f2 = F(1, 'b')



w = sorted([f1,f2])

print(w)