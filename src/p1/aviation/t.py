from unittest.mock import Mock, MagicMock

from p1.aviation.a import Airplane, Location

if __name__ == '__main__':
    # https://docs.python.org/3/library/unittest.mock.html
    p = Airplane()
    p.fly_to = MagicMock(return_value=5)  # overwrite
    g = p.fly_to(Location())
    print(g)
