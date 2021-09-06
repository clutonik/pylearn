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
            self.tail = new_node
            return

        # append new_node to the list
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = new_node
                break
            current_node = current_node.next

    def remove_duplicates(self):
        current_node = self.head
        temp_set = set([current_node.data.name])
        while current_node.next is not None:
            if current_node.next.data.name in temp_set:
                print(
                    f'duplicate picture found: {current_node.next.data.name}')
                current_node.next = current_node.next.next

            if current_node.next is not None:
                temp_set.add(current_node.next.data.name)
                current_node = current_node.next

    def return_nth_node(self, n):
        """
        returns nth node from the tail

        Args:
            n (int): index from tail
        """
        pointer1 = self.head
        pointer2 = self.head

        for i in range(n):
            print(pointer2.data)
            if pointer2 is None:
                return None
            pointer2 = pointer2.next

        print(f'final pointer2: {pointer2.data}')

        # moving both pointers together
        while pointer2 is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1.data

    def partition_list(self, n):
        """
        re-arranges the list based on the specified value.

        Args:
            n (str): value to use for sorting
        """
        # traverse the list and compare the value
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = None

            if current_node.data.name <= n:
                current_node.next = self.head
                self.head = current_node
            else:
                self.tail.next = current_node
                self.tail = current_node

            current_node = next_node


if __name__ == '__main__':
    # Create Linked List
    pictures_list = PictureLinkedList()

    url = 'http://www.test.ca'
    # create head node
    picture1 = Picture('test', url)
    pictures_list.append(picture1)

    # Add more nodes
    picture2 = Picture('test2', url)
    picture3 = Picture('test3', url)
    pictures_list.append(picture2)
    pictures_list.append(picture3)

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

    # Add a duplicate node
    picture7 = Picture('test', url)
    pictures_list.append(picture=picture7)
    print(pictures_list)

    # Remove duplicate Node
    pictures_list.remove_duplicates()
    print(pictures_list)

    # return nth node from tail
    n = 3
    print(f'nth picture from end (n={n}): {pictures_list.return_nth_node(n)}')

    # partition list
    print(pictures_list)
    pictures_list.partition_list('test4')
    print(pictures_list)
