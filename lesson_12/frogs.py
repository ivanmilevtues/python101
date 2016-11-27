import pprint
from collections import deque
from copy import deepcopy


class TreeNode:
    # >>_<<
    def __init__(self, value, parent=None):
        self.value = list(value)
        self.parent = parent
        if not parent:
            self.level = 0
        else:
            self.level = parent.level + 1
        self.children = []

    def add_child(self, value):
        self.children.append(value)


class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def __take_element(self, value):
        stack = deque()
        stack.append(self.root)

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node.value == value:
                return current_node

            for child in current_node.children:
                stack.append(child)

    def add_child(self, parent, child):
        node = self.__take_element(parent)
        node.children.append(TreeNode(child, node))

    def find(self, value):
        return bool(self.__take_element(value))

    def tree_levels(self):
        queue = deque()
        queue.append((0, self.root))

        result = {}

        while(len(queue) != 0):
            level, current_node = queue.popleft()

            if level not in result:
                result[level] = [current_node.parent]
            else:
                result[level].append(current_node.parent)
            for child in current_node.children:
                queue.append((level + 1, child))

        return result


def swap(l, ind1, ind2):
    l[ind1], l[ind2] = l[ind2], l[ind1]


def movement_validator(char_list, index):
    curr_permotation = deepcopy(char_list)
    if char_list[index] == '>':
        if index <= len(curr_permotation) - 3:
            if curr_permotation[index + 1] == '_':
                swap(curr_permotation, index, index + 1)
                return curr_permotation
            if curr_permotation[index + 2] == '_':
                swap(curr_permotation, index, index + 2)
                return curr_permotation
        if index <= len(curr_permotation) - 2:
            if curr_permotation[index + 1] == '_':
                swap(curr_permotation, index, index + 1)
                return curr_permotation
        return False
    else:
        if index >= 2:
            if curr_permotation[index - 1] == '_':
                swap(curr_permotation, index, index - 1)
                return curr_permotation
            if curr_permotation[index - 2] == '_':
                swap(curr_permotation, index, index - 2)
                return curr_permotation
        if index >= 1:
            if curr_permotation[index - 1] == '_':
                swap(curr_permotation, index, index - 1)
                return curr_permotation
        return False


def generate_steps(char_list):
    result_list = []
    for index in range(len(char_list)):
        result = movement_validator(char_list, index)
        if result:
            result_list.append(result)
    return result_list


def generate_children(parent):
    tmp = parent.value
    children_list = generate_steps(parent.value)
    if not len(children_list):
        return

    children_list = ["".join(el) for el in children_list]

    for value in children_list:
        parent.add_child(TreeNode(value, parent))

    if len(parent.children):
        for child in parent.children:
            generate_children(child)


def main():
    a = Tree(">>>_<<")
    generate_children(a.root)
    result_dict = a.tree_levels()
    print(result_dict)
    current_node = result_dict[11][0].children[0]
    solution = []
    while current_node.parent:
        solution.append(current_node.value)
        current_node = current_node.parent
    print(a.root.value)
    for i in solution[::-1]:
        print(i)
    # print(result_dict[8][0].children[0].value)
    # a.add_child(4, 5)
    # a.add_child(10, 8)
    # print(a.find(4))
    # print(a.find(5))
    # print(a.find(90))
    # print(movement_validator(list("_<<><"), 1))
    # print(movement_validator(list(">>_<<"), 0))
    # print(movement_validator(list(">>_<<"), 1))
    # print(movement_validator(list("<<_>>"), 3))


if __name__ == '__main__':
    main()
