
try:
    raise ZeroDivisionError('test error')
except ZeroDivisionError as e:
    print(e)