from enum import Enum


class Animal(Enum):
    DOG = 1
    CAT = 2


print(Animal.DOG)
# <Animal.DOG: 1>

print(Animal.DOG.value)
# 1

print(Animal.DOG.name)
# "DOG"
