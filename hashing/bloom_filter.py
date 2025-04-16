import math
import mmh3
from bitarray import bitarray 

class BloomFilter(object):
    def __init__(self, items_count, fp_prob):
        """
        items_count - количество элементов, которое мы планируем хранить в фильтре Блума.
        fp_prob - желаемая ложно-положительная вероятность.
        """
        self.fp_prob = fp_prob

        # Размер битового массива.
        self.size = BloomFilter.get_size(items_count, fp_prob)

        # Количество хэш-функций.
        self.hash_count = BloomFilter.get_hash_count(self.size, items_count)

        # Формируем битовый массив.
        self.bit_array = bitarray(self.size)

        # Инициализация битового массива нулями.
        self.bit_array.setall(0)

    def add(self, item):
        """
        Добавляет элемент в фильтр Блума.
        """
        for i in range(self.hash_count):
            # Вычисляет индекс используя hash функцию.
            index = mmh3.hash(item, i) % self.size
            print(index)

            # Устанавливает элемент битового массива в True.
            self.bit_array[index] = 1

    def check(self, item):
        """
        Проверяет нахождение элемента в фильтре Блума.
        """
        for i in range(self.hash_count):
            # Вычисляет индекс используя hash функцию.
            index = mmh3.hash(item, i) % self.size

            # Если хотя бы один из элементов установлен в ноль, то возвращаем False.
            if not self.bit_array[index]:
                return False                
        return True

    @staticmethod
    def get_size(items_count, fp_prob):
        """
        Возвращает размер битового массива использую математическую формулу:
        m = -(n * lg(p)) / (lg(2)^2) 
        n - количество элементов, которое мы планируем хранить в фильтре Блума.
        p - вероятность ложно-положительного срабатывания.
        """
        filter_bloom_size = -(items_count * math.log(fp_prob)) / (math.log(2) ** 2)
        return int(filter_bloom_size)
    

    @staticmethod
    def get_hash_count(size, items_count):
        """
        Вычисляет необходимое количество хэш-функций по формуле:
            k = (m/n) * lg(2)
        m - размер битового массива,
        n - количество элементов, которое мы планируем хранить в фильтре Блума.
        """
        filter_bloom_hash_count = (size / items_count) * math.log(2)
        return int(filter_bloom_hash_count)
    
    def __str__(self):
        return self.bit_array.to01()
    

def main():
    bf = BloomFilter(50, 0.01)
    print(1, bf)
    bf.add(bytes(5))
    bf.add(bytes(7))
    print(2, bf)
    print(bf.check(bytes(10)))
    print(bf.check(bytes(5)))
    print(bf.size)


if __name__ == "__main__":
    main()