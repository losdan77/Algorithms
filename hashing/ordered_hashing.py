class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"
    

class HashTable:
    STEP = 1

    def __init__(self, size):
        self.size = size
        self.elements = 0
        # Создаем хэш-таблицу и заполняем её None.
        self.table = [None for i in range(self.size)]

    def _hash(self, key):
        return key % self.size
    
    def add(self, value):
        """
        Добавляем элемент в хэш-таблицу.
        Возбуждаем исключение, если элемент уже есть в таблице.
        """
        key = int(value[1:4])

        # Проверяем заполненность хэш-таблицы.
        if self.elements == self.size:
            raise OverflowError
        
        # Высчитываем начальный индекс для вставки.
        start_index = self._hash(key)

        while True:
            # Проверяем, не пуст ли текущий элемент.
            if not self.table[start_index]:
                # Вставляем элемент в хэш-таблицу.
                self.table[start_index] = DataItem(key, value)
                self.elements += 1
                return
            
            # Проверяем, нет ли элемента с переданным ключом в таблице.
            if self.table[start_index].key == key:
                raise ValueError(f"Ключ {key} уже находится в таблице под индексом {start_index}.)")
            
            # Смотрим, если существующий элемент больше нового.
            if self.table[start_index].key > key:
                # Меняем значения и делаем рехэширование.
                old_item = self.table[start_index]
                
                # Вставляем на текущее место новое значение.
                self.table[start_index] = DataItem(key, value)

                # Запоминаем ключ и значение
                key = old_item.key
                value = old_item.value

            # Переходим к следующей ячейке.
            start_index = self._hash(start_index + HashTable.STEP)

    def find(self, key):
        num_probe = 0
        start_index = self._hash(key)
        
        while True:
            num_probe += 1

            # Проверяем, не пуст ли очередной элемент.
            if not self.table[start_index] or self.table[start_index].key > key:
                return 

            # Проверяем, не находится ли в ячейке целевой элемент.
            if self.table[start_index].key == key:
                return self.table[start_index]

            # Проверяем, не прошли ли мы уже по кругу.
            if num_probe > self.size:
                return 

            # Переходим к следующей ячейке.
            start_index = self._hash(start_index + HashTable.STEP)


    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        for i in range(self.size):
            if self.table[i] is None:
                text += f"{i: 3d}: [--------]\n"
            else:
                text += f"{i: 3d}: {self.table[i]}\n"

        return text


def main():
    example_array = [
        "B617KM39RUS", "B398AB39RUS", "C254HE39RUS", "E123OK39RUS",
        "H637EA39RUS", "O157BA39RUS", "T765KP39RUS", "E389BT39RUS",
        "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
        "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
        "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B513MK39RUS",
    ]

    ht = HashTable(20)
    for value in example_array:
        ht.add(value)
    print(ht)

    # print(ht.find(157))


if __name__ == "__main__":
    main()