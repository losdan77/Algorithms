class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node


    def __str__(self):
        return f'{self.value}'
    

class List:
    def __init__(self):
        self.top = Node()
        self.tail = None


    def add_to_end(self, value):
        current = self.tail

        if current is None:
            self.top.next_node = Node(value)
            self.tail = self.top.next_node
            return
            
        current.next_node = Node(value)     
        self.tail = current.next_node   


    def add_to_start(self, value):
        if self.top.next_node is None:
            self.top.next_node = Node(value)
            self.tail = self.top.next_node
            return
        
        second_node = self.top.next_node
        self.top.next_node = Node(value)
        current = self.top.next_node
        current.next_node = second_node

    
    def add_before_node_by_value(self, value, target):
        prev = self.top
        current = self.top.next_node

        while current:
            if current.value == target:
                prev.next_node = Node(value)
                new_node = prev.next_node
                new_node.next_node = current
                return
            
            prev = current
            current = current.next_node



    def delete(self, value):
        current = self.top.next_node
        prev = self.top

        while current:
            if current.value == value:
                prev.next_node = current.next_node
                return
            
            prev = current
            current = current.next_node
        

    def __str__(self):
        current = self.top.next_node
        values = '['
        while current:
            end = ', ' if current.next_node else ']'
            values += str(current) + end
            current = current.next_node
        return values


def main():
    lst = List()
    lst.add_to_end(6)
    lst.add_to_end(4)
    lst.add_to_end(11)
    lst.add_to_end('ok')
    lst.add_to_end(4)
    lst.add_to_end(228)
    lst.add_to_end(322)
    print(lst)
    lst.delete('ok')
    print(lst)
    lst.add_to_start(111)
    lst.add_to_start(222)
    print(lst)
    lst.add_before_node_by_value(333, 322)
    lst.add_before_node_by_value(444, 11)
    print(lst)

if __name__ == '__main__':
    main()