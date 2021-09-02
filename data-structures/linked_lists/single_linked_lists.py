#!python3

# This is a single linked list implementation.

class Picture:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __repr__(self):
        return 'Picture('+self.name + ',' + self.url + ')'


class PictureNode:
    def __init__(self, data: Picture = None, next=None):
        assert type(data) == Picture, f'You can only add pictures to this list'
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class PictureLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ' -> '.join(map(str, nodes))

    def __iter__(self):
        """
        Allows user to iterate over our linked list

        Yields:
            [PictureNode]: Yields PictureNode() and comes back to get ready for next
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def length(self):
        current_node = self.head
        total = 0
        while current_node != None:
            total += 1
            current_node = current_node.next

        return total

    # TODO:
    # 1. Create a method to insert a node after a specific node
    # 2. Create a method to insert a node before a specific node

    def insert(self, value: Picture, position=None):
        # Create an object of class Node
        new_node = PictureNode(data=value)

        # check if linked list is empty i.e. head = tail = None
        if self.head is None:
            self.head = new_node
            return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        elif position == None:
            current_node = self.head
            while True:
                if current_node.next is None:
                    current_node.next = new_node
                    break
                current_node = current_node.next


if __name__ == '__main__':
    # Create Linked List
    pictures_list = PictureLinkedList()

    url = 'http://www.test.ca'
    # create head node
    picture1 = Picture('test', url)
    node1 = PictureNode(data=picture1)
    pictures_list.head = node1

    # Add more nodes
    picture2 = Picture('test2', url)
    picture3 = Picture('test3', url)
    node2 = PictureNode(data=picture2)
    node3 = PictureNode(data=picture3)
    node1.next = node2
    node2.next = node3

    # Add a new node using insert() method
    picture4 = Picture('test4', url)
    pictures_list.insert(value=picture4)
    print(pictures_list)
