#!/System/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# Filename: total.py
#可变参数(VarArgs)
def total(initial=5, *numbers, **keywords):
    count = initial
    #当我们以星号声明一个形参比如*param,那么这个参数点之后的所有实参会被收 集成一个列表
    for number in numbers:
        count += number
    #以双星号声明一个形参,它会被 收集成一个关键字实参字典
    for key in keywords:
		count += keywords[key]
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100))
