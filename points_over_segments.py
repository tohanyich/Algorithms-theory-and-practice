import sys
from collections import OrderedDict

text = '''4 7
1 3
2 5
5 6'''


def find_points(segments):
    points = []
    for seg in segments.values():
        if points:
            if seg[0] <= points[-1]:
                continue
        points.append(seg[1])

    return points


def main():
    # seg_number = int(input())

    segments = OrderedDict()
    # for key, line in enumerate(sys.stdin):
    for key, line in enumerate(text.split('\n')):
        segments.update({key: [int(x) for x in line.split()]})

    # Передаем в функцию словарь отсортированный по концам отрезков
    points = find_points(OrderedDict(sorted(segments.items(), key=lambda t: t[1][1])))

    print(len(points))
    print(' '.join(map(str, points)))


if __name__ == "__main__":
    main()