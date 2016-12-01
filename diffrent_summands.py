def main():
    n = int(input())
    k = 0
    terms = []
    if n != 1:
        for i in range(1, n+1):
            if k + i < n:
                k += i
                terms.append(i)
            elif k + i == n:
                terms.append(i)
                break
            else:
                terms[-1] = terms[-1] + n - k
                break
    else:
        terms.append(1)

    print(len(terms))
    print(' '.join((str(x) for x in terms)))


if __name__ == "__main__":
    main()