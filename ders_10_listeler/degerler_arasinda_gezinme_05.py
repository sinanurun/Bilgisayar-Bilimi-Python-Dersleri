def my_reversed(lst):
    for i in range(len(lst)-1,-1,-1):
        yield(lst[i])
