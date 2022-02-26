
## MODEL
from dataclasses import dataclass


@dataclass
class Request:
    userid: int


@dataclass
class Client:
    id: int
    name: str

    # def __hash__(self):
    #     return (self.id,self.name).__hash__()


@dataclass
class Employee:
    id: int
    name: str


s = set([Client(1,'a'), Client(1,'a')])
print(s)

for x in s:
    print(x.__hash__())