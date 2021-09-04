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
        if self.head is None:
            return 'List is empty'
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
        """
        returns number of elements/nodes in list

        returns:
            total: number of nodes in list

        """
        current_node = self.head
        total = 0
        while current_node != None:
            total += 1
            current_node = current_node.next

        return total

    def add_after(self, picture: Picture, target_picture: Picture):
        """
        adds a new Picture Node after a specific node

        Args:
            picture (Picture): New Picture to Add
            target_picture(Picture): Picture to add new image after

        Raises:
            Exception: target_picture not found
        """
        assert type(
            picture) == Picture and type(target_picture) == Picture, 'only pictures can be added to this list'

        # check if list is empty
        if self.length() == 0:
            print('list is empty')
            return

        # create PictureNode for linked list
        new_node = PictureNode(data=picture)

        # loop over list
        for node in self:
            if node.data.name == target_picture.name:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(
            "add_after(): picture with name '%s' not found" % target_picture.name)

    def add_before(self, picture: Picture, target_picture: Picture):
        """
        adds a new Picture Node before a specific node

        Args:
            picture (Picture): New Picture to Add
            target_picture(Picture): Picture to add new image before 

        Raises:
            Exception: target_picture not found
        """
        assert type(
            picture) == Picture and type(target_picture) == Picture, 'only pictures can be added to this list'

        # check if list is empty
        if self.length() == 0:
            print('list is empty')
            return

        # create PictureNode for linked list
        new_node = PictureNode(data=picture)

        # loop over list
        for node in self:
            if node.next.data.name == target_picture.name:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(
            "add_before(): picture with name '%s' not found" % target_picture.name)

    def append(self, picture: Picture):
        """
        adds a new Picture Node at the end of the list

        Args:
            picture (Picture): New Picture to Add

        """
        assert type(
            picture) == Picture, 'only pictures can be added to this list'
        # Create an object of class Node
        new_node = PictureNode(data=picture)

        # check if linked list is empty i.e. head = None
        if self.length() == 0:
            self.head = new_node
            return

        # append new_node to the list
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
    pictures_list.append(picture=picture4)
    print(pictures_list)

    # Add a new node after an existing node
    picture5 = Picture('test5', url)
    pictures_list.add_after(picture5, picture3)
    print(pictures_list)

    # Add a new node before an existing node
    picture6 = Picture('test6', url)
    pictures_list.add_before(picture6, picture3)
    print(pictures_list)
