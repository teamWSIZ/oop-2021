

class DangerousError(RuntimeError):
    pass

class CriticalError(DangerousError):
    pass


def foo(x):
    if x==1:
       raise CriticalError()
    if x==2:
       raise DangerousError('x is 2 !!')

if __name__ == '__main__':
    try:
        foo(int(input()))
    except RuntimeError as e:
        print(e)
    finally:
        print('uff')