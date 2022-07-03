#Родионов Д.М. 2 курс ИВТ
import datetime

def print_results(*args, action, result): #объявление функции
    """
    Вывод в табличном виде результатов вычислений
    """
    for arg in args:
        print("| " + str(arg), end=" ")
    print("| " + str(action) + " | ", end="")
    print("res: " + str(result) + " |") #цикл, вывод по агрументам, разделение символом |, объявление рузельтатов
   


def write_log(*args, action=None, result=None, file='calc-history.log.txt'): #создание файла, в который добавляется дата, действие, аргументы, результат
    f = open(file, mode='a', errors='ignore')

    now = datetime.datetime.now()
    now_time = now.strftime("%d-%m-%Y %H:%M")

    f.write(f"{now_time}, {action}: {args} = {result} \n")
    f.close() 