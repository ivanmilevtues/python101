class Node:
    def __init__(self, value, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next = next_

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self):
        self.len = 0

    def add_element(self, data):
        new_node = Node(data)

        if self.len:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.len += 1

    def set_element(self, index, data):
        node = self.index(index)
        node.value = data

    def index(self, index):
        cur_node = self.head

        for i in range(index):
            cur_node = cur_node.next
            if cur_node is None:
                return False
        return cur_node

    def size(self):
        return self.len

    def remove(self, index):
        elem_rm = self.index(index)

        if elem_rm == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
        elif elem_rm:
            elem_rm.prev.next = elem_rm.next
            elem_rm.next.prev = elem_rm.prev
            self.len -= 1
        else:
            return False

    def pprint(self):
        for i in self.len:
            print(i)

    def to_list(self):
        list_res = []
        cur = self.head

        while cur is not None:
            list_res.append(cur.value)
            cur = cur.next

        return list_res

    # add element and index N (Example: ll = [2 => 3 => 4]
    # ll.ad_at_index(1, "New data")
    # ll = [2 => "New data" =>  3 => 4]
    def add_at_index(self, index, data):
        new_node = Node(data)
        next_node = self.index(index)

        next_node.prev.next = new_node
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node

        self.len += 1

    def add_first(self, data):
        new_head = Node(data)

        self.head.prev = new_head
        new_head.next = self.head
        self.head = new_head

    def add_list(self, some_list):
        for i in some_list:
            self.add_element(i)

    def add_linked_list(self, some_linkedList):
        for i in range(some_linkedList.size()):
            self.add_element(some_linkedList.index(i))

    def ll_from_to(self, start_index, end_index):
        result_ll = LinkedList()

        for i in range(start_index, end_index):
            result_ll.add_element(self.index(i))

        return result_ll

    def pop(self):
        result = self.tail

        self.tail = self.tail.prev
        self.tail.next = None
        return result

    def reduce_to_unique(self):
        set_of_elems = list(set(self.to_list()))
        self.head = None
        self.tail = None
        self.add_list(set_of_elems)


def main():
    pass


if __name__ == '__main__':
    main()
