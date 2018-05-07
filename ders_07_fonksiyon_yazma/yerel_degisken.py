x=2
print("1. x =",x)
def fun1(a=15):
    x=10
    print("2. x =",x)
    return a
print("3. x =",x)
def fun2():
    x=20
    print("4. x =",x)
print("5. x =",x)
fun1()
fun2()
print("6. x =",x)