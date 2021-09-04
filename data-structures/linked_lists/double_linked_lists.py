#!python3

# Demonstrate use of double linked lists

# Common Error messages
PICTURE_TYPE_ERROR = 'this list only works with pictures'
EMPTY_LIST_ERROR = 'list is empty'


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
    def __init__(self, data: Picture, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return f'PictureNode({self.data})'


class DoublePictureList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __iter__(self):
        """
        Making double linked list iterable

        Yields:
            [PictureNode]: PictureNode Object
        """
        node = self.head
        while node.next != None:
            yield node
            node = node.next

    def __repr__(self):
        if self.head is None:
            return 'List is empty.'

        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return ' -> '.join(map(str, nodes))

    def append(self, picture: Picture):
        assert type(picture) == Picture, PICTURE_TYPE_ERROR

        # create pictureNode
        new_node = PictureNode(data=picture)

        # Check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # if not empty, traverse the list and get the last node
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        # Append the new node
        new_node.previous = current_node
        current_node.next = new_node
        self.tail = new_node

    def add_before(self, picture: Picture, target_picture: Picture):
        assert type(picture) == Picture and type(
            target_picture) == Picture, PICTURE_TYPE_ERROR

        # check if list is empty
        if self.head is None:
            return EMPTY_LIST_ERROR

        # Create new node
        new_node = PictureNode(data=picture)

        # Loop over list to find the target_picture
        # There are two ways to do it, i.e. one to find the target node directly and accessing
        # the previous element
        current_node = self.head
        while current_node.next != None:
            if current_node.next.data.name == target_picture.name:
                # connect target node with new_node backwards
                current_node.next.previous = new_node
                new_node.next = current_node.next
                new_node.previous = current_node
                current_node.next = new_node
                return
            current_node = current_node.next

        raise Exception('target node %s not found' % target_picture.name)

    def add_after(self, picture: Picture, target_picture: Picture):
        assert type(picture) == Picture and type(
            target_picture) == Picture, PICTURE_TYPE_ERROR

        # check if list is empty
        if self.head is None:
            return EMPTY_LIST_ERROR

        # Create new node
        new_node = PictureNode(picture)

        # Loop over the list to find target_picture
        current_node = self.head
        while current_node.next != None:
            if current_node.data.name == target_picture.name:
                new_node.next = current_node.next
                new_node.previous = current_node
                current_node.next.previous = new_node
                current_node.next = new_node
                return
            current_node = current_node.next

        raise Exception('target node %s not found' % target_picture.name)

    def reverse_traversal(self):
        # check if list is empty
        if self.head is None:
            return EMPTY_LIST_ERROR

        # Loop over the list through its tail
        current_node = self.tail

        while current_node is not None:
            yield current_node.data
            current_node = current_node.previous

    def search_picture(self, picture_name: str):
        # check if list is empty
        if self.head is None:
            return EMPTY_LIST_ERROR

        # Loop over the list through its head
        current_node = self.head
        while current_node.next != None:
            if current_node.data.name == picture_name:
                return current_node
            current_node = current_node.next

        raise Exception('node %s not found' % picture_name)


if __name__ == '__main__':
    picture_list = DoublePictureList()
    print(picture_list)

    # Add a Picture to double linked list
    pic1 = Picture('test1', 'http://test1.ca')
    pic2 = Picture('test2', 'http://test2.ca')
    picture_list.append(pic1)
    picture_list.append(pic2)
    print(picture_list)

    # Add an element before a specific node
    pic3 = Picture('test3', 'http://test3.ca')
    picture_list.add_before(pic3, pic2)
    print(picture_list)

    # Add an element after a specific node
    pic4 = Picture('test4', 'http://test4.ca')
    picture_list.add_after(pic4, pic3)
    print(picture_list)

    # reverse traversal
    print([node for node in picture_list.reverse_traversal()])

    # search a picture
    searched_pic = picture_list.search_picture('test3')
    print(searched_pic)

    # Get next node
    print(searched_pic.previous)
