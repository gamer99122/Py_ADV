# Decorator 裝飾器，沒有小老鼠版本
# def print_func(func):
#     def inner(n, d):
#         if (d == 0):
#             return 0
#         else:
#             return func(n,d)
#     return inner

# def divide(n, d):
#     return n/d

# Result = print_func(divide)(1,0)

# print(Result)

# -----------------------------------------
# Decorator 裝飾器，小老鼠版本
def print_func(func):
    def inner(n, d):
        if (d == 0):
            return 0
        else:
            return func(n,d)
    return inner


@print_func
def divide(n, d):
    return n/d

Result = divide(1,0)

print(Result)