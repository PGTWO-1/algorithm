def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


if __name__ == '__main__':
    a = int(input("Please enter the number 1: "))
    b = int(input("Please enter the number 2: "))
    s = gcd(a, b)
    print(s)
