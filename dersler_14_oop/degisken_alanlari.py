global spam
spam = "oluşturduğum"
global ikinci
def scope_test():
    def tanimlanan():
        global spam
        global ikinci
        ikinci ="ikinci"
        print(spam)
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    tanimlanan()
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

print(spam)

scope_test()
print("In global scope:", spam)
print(ikinci)