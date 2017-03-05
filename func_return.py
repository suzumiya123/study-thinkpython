def count():
    fs = []
    for i in range(1, 4):
        fs.append(lambda : i * i)
    return fs

f1, f2, f3 = count()

print(count())
print(f1())
print(f2())
print(f3())

#这里的i是引用count函数里的for循环里面的变量，循环执行第一次，fs里面放入第一个函数i*i，此时执行此函数的话值是1。
#循环执行第二次，fs里面加入了第二个函数也是i*i，此时fs里面有两个函数，此时执行这两个函数的话都引用此时的i值，计算结果值是4。
#同理，循环第三次时候，fs里面放置了3个函数，都是i* i。 执行这三个函数时候都i都使用此时count函数里的i值，即为3，故结果都为9。
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

def count():
    fs = []
    for i in range(1, 4):
        fs.append(lambda a=i: a * a)
    return fs

f1, f2, f3 = count()

print(count())
print(f1())
print(f2())
print(f3())

#这里是将count里的i值赋给一个内部函数的变量a。返回后fs内的三个函数都是a*a，但a的值是不同的，分别为1、2、3.
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
