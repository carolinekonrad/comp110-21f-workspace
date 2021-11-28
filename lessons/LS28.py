def fun(x: int) -> str:
    if x > 100:
        return '!'
    else:
        return '!' + fun(x % 2)


print(fun(99))