#Родионов Д.М. 2 курс ИВТ
#чтобы тесты были запущены и работали корректно была вызвана функция load_params
import unittest 
from calculate import *
from calculate import load_params

global PARAMS

load_params()

class CalculatorTests(unittest.TestCase):

    global PARAMS

    def mult(self): 
        self.assertEqual(calculate(1.0, 2.0, 3.0, '*', **PARAMS), 6.0) #проверка верности произведения

    def diff(self):
        self.assertEqual(calculate(10, 5, 3, '-', **PARAMS), -18.0) #проверка верности разности

    def divisonZero(self):
        self.assertIsNone(calculate(1.0, 2.0, 0, '/', **PARAMS)) #проверка обработки деления на 0 (должно вернуться None)

    def division(self):
        self.assertEqual(calculate(6, 3, 2, '/', **PARAMS), 1) #проверка верности частного

    def summator(self):
        self.assertEqual(calculate(6, 3, 2, '+', **PARAMS), 11.0) #проверка верности сложения


if __name__ == '__main__': 
    unittest.main()