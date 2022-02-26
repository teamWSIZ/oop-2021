def rrr(fct):
    def r(*args, **kw):
        print(kw)
        print(args)
        return fct(*args, **kw)
    return r


@rrr
def foo(x, **kw):
    print(f'*** x={x}')

foo(5, key='1234')
foo(7)

