import logging
import unittest
import rt_with_exceptions as rt

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8', format="%(asctime)s | %(levelname)s | %(message)s")

#Создаем класс для тестов:
    
class RunnerTest(unittest.TestCase):
    is_frozen = False
    
#Создаем тест работы функции 'walk' относительно рассчитанного значения:
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            first_walker = rt.Runner('Bob', -2)  
            for i in range(10):
                rt.Runner.walk(first_walker)
            self.assertEqual(first_walker.distance, 50, 'Fail')
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner", exc_info=True)
    
#Создаем тест работы функции 'run' относительно рассчитанного значения: 
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')                         
    def test_runner(self):
        try:
            first_runner = rt.Runner(['Petr'])
            for i in range(10):
                rt.Runner.run(first_runner)
            self.assertEqual(first_runner.distance, 100, 'Fail')
            logging.info('"test_runner" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
       
#Создаем тест работы функций 'walk' и 'run' относительно друг друга:
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')     
    def test_challenge(self):
        sec_walker = rt.Runner('Vasya')
        for i in range(10):
            rt.Runner.walk(sec_walker)
        sec_runner = rt.Runner('Georgy')
        for i in range(10):
            rt.Runner.run(sec_runner)
        self.assertNotEqual(sec_walker.distance, sec_runner.distance, 'Fail')
        
#Запускаем код при условии, что он запущен из модуля тестирования:      
if __name__ == '__main__':
    unittest.main()