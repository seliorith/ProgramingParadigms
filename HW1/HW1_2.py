# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_descending(numbers):
    return sorted(numbers, reverse=True)


# Пример использования:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_descending_numbers = sort_descending(numbers)
print("Сортировка по убыванию:", sorted_descending_numbers)
