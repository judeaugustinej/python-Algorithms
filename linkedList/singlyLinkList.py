class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size +=1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True #data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

if __name__ == "__main__":
    myList = LinkedList()
    myList.add(6)
    myList.add(8)
    myList.add(11)
    print(myList)
    print(myList.find(11))
    print(myList.find(111))
