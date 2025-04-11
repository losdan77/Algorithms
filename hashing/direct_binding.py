class Cell:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"[{self.key}:{self.value}]"
    

class HashTable:
    def __init__(self, size):
        """
        Создаем массив и заполняем его связными списками.
        """
        self.size = size
        self.elements = 0

        # Заполняем пустой ячейкой (вершиной связного списка).
        self.buckets = [Cell(None, None, None) for i in range(self.size)]

    def _hash(self, key):
        """
        Вычисляем хэш (индекс элемента массива).
        """
        return int(key) % self.size
    
    def _find_cell_before(self, key):
        """
        Возвращает элемент связного списка перед искомым.
        Или None если искомого элемента нет.
        """

        # Получаем индекс элемента массива, используя хэширование.
        bucket_num = self._hash(key)
        # Получаем вершину подходящего связного списка.
        top = self.buckets[bucket_num]

        # Ищем элемент связного списка по ключу.
        cell = top
        while cell.next is not None:
            if cell.next.key == key:
                # Возвращаем элемент.
                return cell
            cell = cell.next

        # Если элемента нет, то возвращаем None.
        return None
    
    def get(self, key):
        """
        Возвращает элемент по его ключу.
        Или None если элемента нет.
        """

        # Получаем элемент предшествующий искомому.
        cell_before = self._find_cell_before(key)

        if not cell_before:
            return None
        
        # Возвращаем ячейку связного списка.
        return cell_before.next

    def insert(self, value):
        """
        Вставляем новое значение в хэш-таблицу.
        """
        key = value[1:4]

        # Ищем значение в хэш-таблице, если оно уже есть, то вызываем исключение.
        if self.get(key):
            raise ValueError(f"Ключ {key} уже находится в хэш-таблице.")
        
        # Получаем подходящий связный список для вставки нового элемента.
        bucket_num = self._hash(key)
        linked_list = self.buckets[bucket_num]

        # Добавляем новую ячейку в начало связного списка.
        new_cell = Cell(key, value, linked_list.next)
        linked_list.next = new_cell

        # Увеличиваем счетчик элементов хэш-таблицы.
        self.elements += 1
    
    def delete(self, key):
        """
        Удаляет элемент из хэш-таблицы по ключу.
        Возбуждает исключение, если элемента в хэш-таблице нет.
        """
        
        # Получаем элемент, который стоит перед тем, который нужно удалить.
        before_cell = self._find_cell_before(key)

        # Если такого нет, то возбуждаем исключение.
        if not before_cell:
            raise ValueError(f"Ключа {key} нет в хэш-таблице")
        
        # Удаляем элемент из связного списка.
        before_cell.next = before_cell.next.next

        # Обновляем количество элементов в хэш-таблице.
        self.elements -= 1

    def change_size(self, new_size):
        """
        Изменяет размер хэш таблицы и делает рехэширование.
        """

        # Создаем новый массив.
        self.size = new_size
        new_buckets = [Cell(None, None, None) for i in range(self.size)]
        
        # Делаем рехэширование.
        for cell in self.buckets:
            cell = cell.next
            while cell:
                new_bucket_num = self._hash(cell.key)
                new_linked_list = new_buckets[new_bucket_num]

                new_cell = Cell(cell.key, cell.value, new_linked_list.next)
                new_linked_list.next = new_cell

                cell = cell.next
        # Заменяем старый массив новым.
        self.buckets = new_buckets

    def __str__(self):
        """
        Возвращает текстовое представление хэш таблицы.
        """
        text = ""
        for _, cell in enumerate(self.buckets):
            text += f"{_}:"
            cell = cell.next
            while cell is not None:
                text += f" {cell}"
                cell = cell.next
            text += "\n"
        return text 


def main():
    example_array = ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                     "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS",
                     "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
                     "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
                     "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B516MK39RUS",]
    
    ht = HashTable(10)
    for value in example_array:
        ht.insert(value)
    print(ht)
    
    ht.delete("313")
    print(ht)

    ht.change_size(20)
    print(ht)


if __name__ == "__main__":
    main()