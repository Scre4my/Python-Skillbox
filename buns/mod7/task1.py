def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            if len(args) < 1:
                return "Not enough arguments"
            else:
                return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(-10))