# put your python code here
def main():
    str = input()

    l_number, str_long = map(int, str.split())
    letters = {}
    for i in range(l_number):
        key, code = input().split(': ')
        letters[code] = key

    code_str = input()
    f_code = ''
    res = ''
    for s in code_str:
        f_code += s
        next_letter = letters.get(f_code)
        if next_letter:
            f_code = ''
            res += next_letter

    print(res)

if __name__ == "__main__":
    main()