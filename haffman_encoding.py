import heapq
from collections import Counter


class Node:
    def __init__(self, left=None, right=None, data=None, value=None, code=''):
        self.left = left
        self.right = right

        self.data = data
        self.value = value
        self.code = code

    def __str__(self):
        return 'Node ['+str(self.data)+']'


class Tree:
    def __init__(self):
        self.root = None  # корень дерева
        self.encoding_dict = {}

    def NewNode(self, data):
        return Node(None, None, data, None)

    # /* функция для вычисления высоты дерева */
    def height(self, node):
        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)

            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1

    # /* функция для распечатки элементов на определенном уровне дерева */
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print('{} {} {}'.format(root.data, root.value, root.code))
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    # /* функция для распечатки дерева */
    def print_level_order(self):
        h = self.height(self.root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            i += 1

    def set_code_given_level(self, root, level, code):
        if root is None:
            return
        if level == 1:
            root.code = code
            if len(root.data) == 1:
                self.encoding_dict.update({root.data: root.code})
        elif level > 1:
            self.set_code_given_level(root.left, level - 1, code + '0')
            self.set_code_given_level(root.right, level - 1, code + '1')

    def set_all_codes(self):
        h = self.height(self.root)
        i = 1
        while (i <= h):
            self.set_code_given_level(self.root, i, self.root.code)
            i += 1

def main():
    # in_str = input()
    in_str = 'aaaccc'
    letters_freq = Counter(in_str)

    heap = []
    for letter, freq in letters_freq.items():
        heapq.heappush(heap, [freq, letter])

    print(heap)

    code_tree = Tree()
    # Если только один символ
    if len(heap) == 1:
        root = heapq.heappop(heap)
        code_tree.root = Node(data=root[1], value=root[0], code='0')
    else:
        while heap:
            if len(heap) > 1:
                left = heapq.heappop(heap)
                right = heapq.heappop(heap)

                if len(left) > 2:
                    l_node = Node(left[2].left, left[2].right, left[1], left[0])
                else:
                    l_node = Node(data=left[1], value=left[0])

                if len(right) > 2:
                    r_node = Node(right[2].left, right[2].right, right[1], right[0])
                else:
                    r_node = Node(data=right[1], value=right[0])

                root_node = Node(l_node, r_node, left[1] + right[1], left[0] + right[0])
                heapq.heappush(heap, [left[0] + right[0], left[1] + right[1], root_node])
            else:
                code_tree.root = heapq.heappop(heap)[2]

    code_tree.set_all_codes()
    # code_tree.print_level_order()
    # print(code_tree.encoding_dict)

    # Закодируем строку
    new_str = ''
    for l in in_str:
        new_str += code_tree.encoding_dict[l]

    print('{} {}'.format(len(code_tree.encoding_dict), len(new_str)))
    for key, code in sorted(code_tree.encoding_dict.items(), key=lambda t: t[0]):
        print('{}: {}'.format(key, code))
    print(new_str)

if __name__ == "__main__":
    main()