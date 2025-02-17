class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node


    def __str__(self):
        return str(self.value)
    

class SortedList:
    '''При добавлении элемента, он сразу встает на нужное место и список всегда отсортирован,
    такое решение имеет сложность O(n) и может быть рационально использовано, если функция 
    сортировки необходимо будет вызывать чаще или равно функции вставки'''
    def __init__(self):
        '''Max value for element in List is 1000'''
        self.top = Node()
        self.bottom = Node(1000)
        self.top.next_node = self.bottom

    
    def append(self, value):
        current = self.top

        while current.next_node.value < value:
            current = current.next_node

        new_node = Node(value)
        new_node.next_node = current.next_node
        current.next_node = new_node

    
    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None and current.value < 1000:
            end = ", " if current.next_node and current.next_node.value < 1000 else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


class List:
    def __init__(self, value = None, next_node = None):
        self.top = Node()


    def append(self, value):
        current = self.top
        while current.next_node:
            current = current.next_node

        current.next_node = Node(value)


    def sort(self):
        new_top = Node()
        current = self.top

        while current.next_node:
            max_after_me = current
            max_value = max_after_me.next_node.value

            after_me = current.next_node
            while after_me.next_node:
                if after_me.next_node.value > max_value:
                    max_after_me = after_me
                    max_value = after_me.next_node.value
                after_me = after_me.next_node

            max_node = max_after_me.next_node
            max_after_me.next_node = max_node.next_node

            max_node.next_node = new_top.next_node
            new_top.next_node = max_node

        self.top = new_top


    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


def main():
    lst = SortedList()
    lst.append(1)
    lst.append(10)
    lst.append(3)
    lst.append(2)
    lst.append(100)
    print(lst)


    lst_2 = List()
    lst_2.append(1)
    lst_2.append(10)
    lst_2.append(3)
    lst_2.append(2)
    lst_2.append(100)
    print(lst_2)
    lst_2.sort()
    print(lst_2)


if __name__ == '__main__':
    main()