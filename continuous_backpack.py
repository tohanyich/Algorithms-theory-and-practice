import sys
from collections import OrderedDict

first_str = '''3 50'''
text = '''60 20
100 50
120 30'''


def calc_max_cost(volume, objects):
    cost = 0.0
    for obj_cost, obj_volume, obj_value in objects.values():
        if volume > obj_volume:
            cost += obj_cost
            volume -= obj_volume
        else:
            cost += volume * obj_value
            break

    return cost


def main():
    # obj_number, volume = [int(x) for x in input().split()]
    obj_number, volume = [int(x) for x in first_str.split()]

    objects = OrderedDict()
    # for key, line in enumerate(sys.stdin):
    for key, line in enumerate(text.split('\n')):
        temp_obj = [int(x) for x in line.split()]
        temp_obj.append(float(temp_obj[0])/float(temp_obj[1]))
        objects.update({key: temp_obj})

    # Передаем в функцию словарь отсортированный по jnyjcbntkmyjq cnjbvjcnb
    objects = OrderedDict(sorted(objects.items(), key=lambda t: t[1][2], reverse=True))
    print('{:.3f}'.format(calc_max_cost(volume, objects)))


if __name__ == "__main__":
    main()