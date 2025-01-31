# Динамические массивы в Python резервируют дополнительные ячееки оперативной памяти 
# (поверх заполненых ячеек), чтобы облегчить операцию вставки. Если не получается
# продлить массив в смежных ячейках памяти, то выбирается более свободное место, а из 
# старого места хранения массива, ячейки очищаются. Связанные списки могут храниться в
# произвольных ячейках памяти, потому что у них есть ссылки, на следующие элементы
import random

class MyArray:
    def __init__(self, *args):
        self.items = [*args]
        self.index = 0
        self.len = len(self.items)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= self.len:
            raise StopIteration
        element = self.items[self.index]
        self.index += 1
        return element
    
    def __max__(self):
        return max(self.items)
    
    def __sum__(self):
        return sum(self.items)
    
    def __min__(self):
        return min(self.items)
    
    def avg(self):
        return sum(self.items)/self.len
        
    def __len__(self):
        return self.len
    
    def __str__(self):
        return str(self.items)
        
    def append(self, value):
        self.len += 1
        self.items.append(value)

    def pop(self):
        self.len -= 1
        self.items.pop()

    def has(self, value):
        if value in self.items:
            return True
        return False
    
    def get_random(self):
        return random.choice(self.items)
    

def main():
    lst = MyArray(1, 2, 3)
    lst.append(4)
    lst.append(5)
    print(f'array lenght = {len(lst)}')
    print(lst)
    lst.pop()
    print(lst)
    print(lst.has(4))
    print(f'random element = {lst.get_random()}')
    print(f'max elememt = {max(lst)}')
    print(f'min element = {min(lst)}')
    print(f'sum elements = {sum(lst)}')
    print(f'avg element = {lst.avg()}')

    lst.append(4)
    lst.append(5)
    print(lst)
    for _ in lst:
        print(_)


if __name__ == '__main__':
    main()