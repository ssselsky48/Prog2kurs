from calcprint import *
import calcprint
import sys
# average
PARAMS = {'precision': None, 
        'output_type': None, 
        'possible_types': None,
        'dest': None} #объявление словаря, в который будут записаны параметры

def load_params(file="params.ini"): #функция записи параметров из флайла в словарь
    '''
        Функция записи параметров из файла в словарь PARAMS
        На вход поступает имя файла, в процессе выполнения 
        Параметры построчно записываются в PARAMS. 
        Функция ничего не возвращает
    '''
    global PARAMS
    try:
        f = open(file, mode='r', errors='ignore')
        lines = f.readlines()
        for l in lines:
            param = l.split('=')
            param[1] = param[1].strip('\n')

            if (param[0] != 'dest'):
                param[1] = eval(param[1])

            PARAMS[param[0]] = param[1]
    except FileNotFoundError:
        print("Файл с параметрами не найден!")
        sys.exit() #записывает парамтры файла в словарь


def convert_precision(prec):
    ''' 
        Функция, конвертирующая заданную точность:
        0.000001 -> 6
        >>> convert_precision(0.00000001)
        8
        >>> convert_precision(0.001)
        3
    ''' #тестирование
    res = 0
    while (prec < 1):
        prec *= 10
        res += 1
    return res #функция преобразования заданной точности в целочисленный формат


def user_input(): 
    args = []

    while True:
        val = input("Enter value: ")  # '1,24'
        # здесь мы можем упасть потому что тип, который ввел пользователь у нас не работает
        try:
            if val == "":
                break
            val = float(val)
        except ValueError:
            print(
                "Введите число в правильном формате (разделитель дробной части '.' "
            )
        else:
            args.append(val) 

    print(args)
    if len(args) <= 1:
        return

    # проверяем на допустимость значений
    print("Введите действие")
    print("Доступные действия: +, -, *, /, average")
    action = input("action: ")

    # потенциально в этом месте что-то может пойти не так как надо
    try:
        res = calculate(*args, action, **PARAMS)
    except Exception:
        print("Ошибка вычисления. Результат не определен") 

    res = calculate(*args, action, **PARAMS)
    calcprint.print_results(*args, action = action, result = res)
    calcprint.write_log(*args, action = action, result = res, file=PARAMS['dest']) #"красивый" вывод, запись в файл, добавлена операция среднего ариф-го


def calculate(*args, **kwargs): #основная функция калькулятора
    precision = convert_precision(kwargs['precision'])
    output_type = kwargs['output_type']

    action = args[-1]
 
    if (action == '+'): #слложение
        result_sum = sum(args[0:len(args) - 1])
        if type(result_sum) is not output_type:
            result_sum = output_type(result_sum)
        return round(result_sum, precision)

    if (action == '-'): #разность
        result_diff = args[0]
        for n in args[1:len(args) - 1]:
            result_diff -= n
        if type(result_diff) is not output_type:
            result_diff = output_type(result_diff)
        return result_diff

    if (action == '*'): #произведение
        res = 1
        for n in args[0:len(args) - 1]:
            res *= n
        return round(res, precision)

    if (action == '/'): #частное
        result_division = args[0]
        for n in args[1:len(args) - 1]:
            if n == 0:
                print("Division Error")
                return None
            result_division /= n
        if type(result_division) is not output_type:
            result_division = output_type(result_division)
        return round(result_division, precision)

    if (action == 'average'): #среднее арифм-ое
        result_av = sum(args[0:len(args) - 1]) / (len(args) - 1)
        if type(result_av) is not output_type:
            result_sum = output_type(result_av)
        return round(result_av, precision)


if __name__ == "__main__": #вызывает следующие 2 функции при условии что программа запущена
    load_params()
    user_input()