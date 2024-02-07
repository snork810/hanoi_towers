'''представим что у нас есть три столба и три блока (в будущем это количество соответственно должно иметь
возможность масштабироваться). Столбы - массивы, блоки - для начала кортеж из названия и площади. Задача 
переместить блоки между массивами с проверками, можно ли положить данный кортеж в данный массив на основе 
площади объекта. Если площадь последнего элемента массива меньше, чем площадь перемещаемого объекта - класть
блок в данный массив нельзя'''
# def move(arr1:list, arr2:list):
#     if arr2 == [] or arr2[-1] > arr1[-1]:
#         arr2.append(arr1[-1])
#         arr1.remove(arr1[-1])
#     else:
#         None
#     return arr1, arr2
# blocks = [300, 200, 100]
# def move_blocks(*args):

#     stolb1 = blocks
#     stolb2 = []
#     stolb3 = []
#     while len(stolb2) != 3 or len(stolb3) != 3:
#         move(stolb1, stolb2)
#         move(stolb1, stolb3)
#         move(stolb2, stolb3)
#         move(stolb1, stolb2)
#         move(stolb3, stolb1)
#         move(stolb3, stolb2)
#         move(stolb1, stolb2)
#         print(stolb1, stolb2, stolb3)

# move_blocks(blocks)

