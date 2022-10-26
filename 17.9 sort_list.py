
### ЗАДАНИЕ 17.9.1

print ()
print (' Эта программа создаёт отсортированный список из произвольной числовой (и не очень) последовательности,')
print (' а также устанавливает соответствующую порядковую позицию в этом списке для любого другого нового числа.')
print (' На ввод допустимы как целые числа, так и числа с плавающей точкой (запятой)')
print ()


### преобразование введенных значений в числа с заменой возможных запятых на точки и игнорированием нечисловых значений
def str2num (s):
    s = s.replace(',','.')
    try:
        dec = float (s)
        if dec - int (dec) == 0:
            dec = int (dec)
        return dec
    
    except:
        pass


### сортировка списка по возрастанию с помощью встроенной функции - sorted ()
def sort_UP (lst):
    return sorted (lst)


### двоичный поиск элемента в списке
def binary_search (array, element, left, right):

    # середина списка
    middle = (left + right) // 2
    
    # все числа одинаковые
    if array [left] == array [right] == element:
        return 'любым, поскольку все числа одинаковые'

    # число больше последнего в списке или равно ему
    if element >= array [right]: 
        return '[' + str (right + 1) + '] после значения ' + str (array [right])

    # число меньше первого в списке или равно ему 
    if element <= array [left]:
        return '[' + str (left) + '] перед значением ' + str (array [left])
   
    # если число непосредственно следующее за серединным
    if array [middle] == element: 
        return '[' + str (middle + 1) + '] между значениями ' + str (array [middle]) + ' и ' + str (array [middle + 1]) 
    
    # если число меньше серединного
    elif element < array [middle]: 
        # рекурсивно ищем в левой половине
        return binary_search (array, element, left, middle-1)
    
    # если число больше серединного
    elif element > array [middle]:
        # ищем в правой
        return binary_search (array, element, middle+1, right)


### получение последовательности в виде строки
input_string = input (' Запишите через пробел любые числа: ')
print ()

### преобразование строки в список 
input_list = input_string.split()

### конвертация значений списка в числа и добавление их в новый числовой список
numbers = []
for item in input_list:
    num = str2num (item)
    if num == 0 or num:
        numbers.append (num)
           
### сортирвка по возрастанию
numbers = sort_UP (numbers)

print (' В данной последовательности распознаны следующие числа (в порядке возрастания):')
print ('', numbers)
print ()

### запрос одного произвольного числа
num = None
while not (num or num == 0):
    num = str2num (input (' Введите одно корректное произвольное число: '))
  
print ()

### поиск позиции введенного числа в списке
pos = binary_search (numbers, num, 0, len (numbers)-1)

print (' Это число займёт в списке позицию с индексом', pos)
print ()

numbers.append (num)
numbers = sort_UP (numbers)

print (' Дополненный список будет выглядеть так: ')
print ('', numbers)
print ()

