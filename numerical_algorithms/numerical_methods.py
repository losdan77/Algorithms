from math import sin


WIDTH = 0.1 # Ширина прямоугольника/трапеции
ORIGINAL_SQUARE = 18.42 # Значение полученное интегрированием


def get_y(x):
    """
    Получаем Y по значению X в соответствии с формулой
    """
    return 1 + x + sin(2 * x)


def rectangle_square(x):
    """
    Вычисляем площадь прямоугольника
    """
    return WIDTH * get_y(x)

def trapezoid_square(x):
    """
    Вычисляем площадь трапеции
    """
    y1 = get_y(x)
    y2 = get_y(x + WIDTH)
    return WIDTH * ((y1 + y2) / 2)


def error(square):
    """
    Вычисление погрешности
    """
    return 100 - (square * 100 / ORIGINAL_SQUARE)


def main():
    # Начальные значения площадей
    r_square = t_square = 0

    # Цикл с 0 до 5, с шагом WIDTH
    x = 0 
    while x < 5:
        r_square += rectangle_square(x)
        t_square += trapezoid_square(x)

        x += WIDTH

    print(f"По формуле прямоугольников: {r_square:.2f} ({error(r_square):.2f}%)")
    print(f"По формуле трапеций:        {t_square:.2f} ({error(t_square):.2f}%)")


if __name__ == "__main__":
    main()
