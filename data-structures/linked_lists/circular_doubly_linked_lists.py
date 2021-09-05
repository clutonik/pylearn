#!python3

# Common Error messages
PICTURE_TYPE_ERROR = 'this list only works with pictures'
PICTURE_NOT_FOUND_ERROR = 'target picture node not found'
EMPTY_LIST_ERROR = 'list is empty'


class Picture:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __repr__(self):
        return 'Picture(name=' + self.name + ', url=' + self.url + ')'

    def __str__(self):
        return f'Picture({self.name}, {self.url})'


class PictureNode:
    def __init__(self, data: Picture, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return f'PictureNode({self.data})'


class CircularDoublePictureList():
    def __init__(self, head=None, tail=None):
        self.head = head

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
            if node.next == self.head:
                break
            node = node.next
        return ' -> '.join(map(str, nodes))

    def append(self, picture: Picture):
        """
        Appends a new picture to the list

        Args:
            picture (Picture): new picture to add
        """
        assert type(picture) == Picture, PICTURE_TYPE_ERROR

        # Create pictureNode
        new_node = PictureNode(data=picture)

        # check if list is empty
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            new_node.previous = self.head
            return

        # if list is not empty
        current_node = self.head
        while current_node is not None:
            print(current_node)
            if current_node.next == self.head:
                current_node.next = new_node
                new_node.next = self.head
                new_node.previous = current_node
                return
            current_node = current_node.next

    def add_before(self, picture: Picture, target_picture: Picture):
        """
        Adds a new picture before a specific picture node

        Args:
            picture (Picture): new picture to add
            target_picture (Picture): target picture to search in the list

        Raises:
            Exception: List is empty if there is no element in list
            Exception: target picture not found
        """
        assert type(picture) == Picture and type(
            target_picture) == Picture, PICTURE_TYPE_ERROR

        # check if list is empty
        if self.head is None:
            raise Exception(EMPTY_LIST_ERROR)

        # new node
        new_node = PictureNode(data=picture)
        # Loop through list and find the target_picture
        current_node = self.head
        while current_node.next is not None:
            if current_node.data.name == target_picture.name:
                new_node.next = current_node
                new_node.previous = current_node.previous
                current_node.previous.next = new_node
                return
            if current_node.next == self.head:
                break
            current_node = current_node.next

        raise Exception(PICTURE_NOT_FOUND_ERROR)

    def add_after(self, picture: Picture, target_picture: Picture):
        """
        Adds a new picture after a specific picture node

        Args:
            picture (Picture): new picture to add
            target_picture (Picture): target picture to search in the list

        Raises:
            Exception: List is empty if there is no element in list
            Exception: target picture not found
        """
        assert type(picture) == Picture and type(
            target_picture) == Picture, PICTURE_TYPE_ERROR

        # check if list is empty
        if self.head is None:
            raise Exception(EMPTY_LIST_ERROR)

        # new node
        new_node = PictureNode(data=picture)
        # Loop through list and find the target_picture
        current_node = self.head
        while current_node.next is not None:
            if current_node.data.name == target_picture.name:
                new_node.next = current_node.next
                new_node.previous = current_node
                current_node.next.previous = new_node
                current_node.next = new_node
                return
            if current_node.next == self.head:
                break
            current_node = current_node.next

        raise Exception(PICTURE_NOT_FOUND_ERROR)


if __name__ == '__main__':
    pictures_list = CircularDoublePictureList()
    pic1 = Picture('test1', 'http://test1.ca')
    pictures_list.append(pic1)
    print(pictures_list)

    pic2 = Picture('test2', 'http://test2.ca')
    pictures_list.append(pic2)
    print(pictures_list)

    pic3 = Picture('test3', 'http://test3.ca')
    pictures_list.add_before(pic3, pic2)
    print(pictures_list)

    pic4 = Picture('test4', 'http://test4.ca')
    pictures_list.add_after(pic4, pic3)
    print(pictures_list)
