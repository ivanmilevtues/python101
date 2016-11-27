class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.children = []
        self.curr_height = 0

    def add_child(self, child):
        self.children.append(child)

    def not_empty(self):
        return len(self.children)


class Tree:

    def __init__(self, root):
        self.root = root
        self.h = 0
        self._size = 1

    def add_child(self, parent, child):
        parent_elem = self.get_elem(parent, [], self.root)
        parent_elem.children.append(Node(child, parent_elem))
        self._size += 1

    def get_elem(self, element, visit, start):
        # if not start:
        #     start = self.root
        visit.append(start)
        if start.value == element:
            return start
        if len(visit) == self._size:
            return False
        if start.not_empty():
            for child in start.children:
                if child not in visit:
                    curr_child = self.get_elem(element, visit, child)
                    if curr_child:
                        return curr_child

    def find(self, x):
        return bool(self.get_elem(x, [], self.root))

    def take_height(self, start=None, height=0):
        if not start:
            start = self.root
        if start.not_empty():
            height += 1
            for i in start.children:
                self.take_height(i, height)
        elif height > self.h:
            self.h = height
        return height

    def height(self):
        self.take_height()
        print(self.h)

    def count_nodes(self):
        pass

    def tree_levels(self):
        pass


def main():
    a = Tree((Node(4)))
    a.add_child(4, 1)
    a.add_child(1, 3)
    a.add_child(3, 89)
    a.add_child(4, 103)
    a.add_child(103, 56)
    # a.add_child(56, 78)
    print(a.find(3))
    print(a.find(5))
    print(a.find(103))
    a.height()

if __name__ == '__main__':
    main()
