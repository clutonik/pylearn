#!python3

# Circular single linked lists
# they don't forget how they started
class Picture:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __repr__(self):
        return 'Picture(name=' + self.name + ', url=' + self.url + ')'

    def __str__(self):
        return f'Picture({self.name}, {self.url})'

    # TODO: Implement eq function


class PictureNode:
    def __init__(self, data: Picture, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class CircularPictureList():
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        if self.head is None:
            return 'List is empty.'

        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            if node.next == self.head:
                break
            node = node.next
        return ' -> '.join(map(str, nodes))

    def __iter__(self):
        """
        Making CircularPictureList iterable

        Yields:
            [PictureNode]: PictureNode Object
        """
        node = self.head
        while node.next != self.head:
            yield node
            node = node.next

    def length(self):
        """
        returns number of nodes in this linked list

        Returns:
            int: number of nodes
        """
        total = 0
        if self.head is None:
            return total

        current_node = self.head

        while True:
            if current_node.next == self.head:
                total += 1
                return
            current_node = current_node.next

        return total

    def append(self, picture: Picture):
        """
        adds a new picture at the end of the list        

        Args:
            picture (Picture): New picture object to insert
        """
        assert type(
            picture) == Picture, 'Only pictures can be appended to this list'

        # create PictureNode
        new_node = PictureNode(data=picture)

        # check if list is empty
        if self.length() == 0:
            self.head = new_node
            new_node.next = new_node
            return

        # if not empty, traverse the list and add new node after the last element in list
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = self.head

    def add_after(self, picture: Picture, target_picture: Picture):
        """
        adds a new picture after the specified target picture

        Args:
            picture (Picture): new picture to add
            target_picture (Picture): existing picture to add new node after
        """
        assert type(picture) == Picture and type(
            target_picture) == Picture, 'This list only works with pictures'

        # Check if list is empty
        if self.length() == 0:
            return 'List is empty'

        # Create PictureNode
        new_node = PictureNode(data=picture)

        # Traverse the list and find the target picture
        current_node = self.head
        for node in self:
            if node.data.name == target_picture.name:
                new_node.next = node.next
                node.next = new_node
                return

    def add_before(self, picture: Picture, target_picture: Picture) -> str:
        """
        adds a new picture before the specified target picture

        Args:
            picture (Picture): new picture to add
            target_picture (Picture): existing picture to add new node before
        """
        assert type(picture) == Picture and type(
            target_picture) == Picture, 'This list only works with pictures'

        # check if list is empty
        if self.length() == 0:
            return 'List is empty'

        # create PictureNode
        new_node = PictureNode(data=picture)

        # traverse the list and find target picture
        for node in self:
            if node.next.data.name == target_picture.name:
                new_node.next = node.next
                node.next = new_node
                return


if __name__ == '__main__':
    # initialize circular linked list
    pictures_list = CircularPictureList()
    print(f'Original Length: {pictures_list.length()}')

    # append a new picture
    pictures_list.append(Picture('test1', 'http://test1.ca'))
    pictures_list.append(Picture('test2', 'http://test2.ca'))
    pictures_list.append(Picture('test3', 'http://test3.ca'))
    print(pictures_list)

    # add a node after a specific node
    pictures_list.add_after(
        Picture('test4', 'http://test4.ca'), Picture('test2', 'http://test2.ca)'))

    print(pictures_list)

    # add a node before a specific node
    pictures_list.add_before(
        Picture('test5', 'http://test5.ca'), Picture('test4', 'http://test4.ca)'))

    print(pictures_list)
