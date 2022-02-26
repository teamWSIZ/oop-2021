import io

def read_sth():
    try:
        with open('ab.txt', 'r') as f:
            print(type(f))  # <class '_io.TextIOWrapper'>
            print(f.buffer.closed)
            raise FileNotFoundError()
            w = io.TextIOWrapper  # < _TextIOBase < _IOBase
            e1 = FileNotFoundError  # < OSError < Exception
            e2 = IsADirectoryError  # < OSError
        print(f.buffer.closed)
    except RuntimeWarning as e:
        print(e)
    finally:
        print('->', f.buffer.closed)


read_sth()


