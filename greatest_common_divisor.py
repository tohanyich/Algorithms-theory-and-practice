def gcd(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)

    return gcd(b % a, a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()