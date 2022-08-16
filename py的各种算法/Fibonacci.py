def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    s = int(input("Please enter the number:"))
    result = fibonacci(s)
    print("The value is %d" % result)
