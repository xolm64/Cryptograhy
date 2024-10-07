
def sred(*args):
    sum=0
    n=0
    for i in args:
        sum = sum+i
        n= n+1
    a = sum/n
    return a

print(sred(2,4,5,7))
