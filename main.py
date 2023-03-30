# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
# Подсказка
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение

array = [int(x) for x in input("Введите числа от 1 до 100 через пробел: ").split()]

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(array))


def binary_search(array, element, left, right):
    if left > right:
        return left, right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1, middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

while True:
    try:
        element = int(input("Введите число от 1 до 100: "))
        if element < 0 or element > 100:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неверный диапазон!")

print(binary_search(array, element, 0,  len(array)))