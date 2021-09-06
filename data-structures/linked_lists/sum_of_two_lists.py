#!python3

# Two numbers are represented as linked lists, where each node contains a single digit.
# The digits are stored in reverse order such that the 1's digit is at the head of the list.
# write a function that adds the two numbers(lists) and returns the sum as linked list.

class Node:
    def __init__(self, value: int, next=None):
        self.data = value
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        if self.head is None:
            return 'List is empty'
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ' -> '.join(map(str, nodes))

    def append(self, value: int):
        # create new node
        new_node = Node(value)

        # check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # add an element at the end
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = new_node
                break
            current_node = current_node.next

    def get_number(self):
        current_node = self.head
        number = ""
        while current_node is not None:
            number = number + str(current_node.data)
            current_node = current_node.next

        return int(number[::-1])


if __name__ == '__main__':

    list1 = LinkedList()
    list1.append(7)
    list1.append(1)
    list1.append(6)
    print(list1)
    print(list1.get_number())

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(2)
    print(list2)
    print(list2.get_number())

    total = list1.get_number() + list2.get_number()
    total_list = LinkedList()

    for s in str(total)[::-1]:
        total_list.append(s)

    print(total_list)
