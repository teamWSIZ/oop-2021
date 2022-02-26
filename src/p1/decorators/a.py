def profile(fct):
    def wrapper(*args, **kw):
        print('start')
        ret = fct(*args, **kw)
        print(f'end {args[0]}')
        return ret
    return wrapper

@profile
def foo(x):
    print(f'x={x}')
    if x==7:
        raise RuntimeError('ha!')

f = profile(print)
f('10')

foo(5)
foo(7)

