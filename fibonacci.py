# число Фибоначчи
def fib(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


# Последняя цифра числа Фибоначчи
def fib_digit(n):
    assert n >= 0

    fib_digits = [0, 1]
    if n < 2:
        return n

    for i in range(2, n+1):
        fib_digits.append((fib_digits[i-1] + fib_digits[i-2]) % 10)

    return fib_digits[n]


def main():
    n = int(input())
    print(fib(n))
    # print(fib_digit(n))


if __name__ == "__main__":
    main()