def get_sum(*args):

    s=0
    for elem in args:
        s=s+elem
    return s

print(get_sum(12,6,8,56,9,45))


def test(**kwargs):
        print(kwargs)

test(a=1, b=2, c=6)   