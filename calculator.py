from utils import is_number
class Calculator:
    def read_input(self):
        first_number = input("Введите первое число (или 'exit' для выхода): ")
        if first_number.lower() == 'exit':
            exit()
        operation = input("Введите операцию (+, -, *, /): ")
        second_number = input("Введите второе число: ")
        if not is_number(first_number) or not is_number(second_number):
            print("Пожалуйста, введите корректные числа.")
            return
        first_number = float(first_number)
        second_number = float(second_number)
        result = self.calculate(first_number, operation, second_number)
        if result is not None:
            print(f"Результат: {result}")
    def calculate(self, first_number, operation, second_number):
        if operation == '+':
            return first_number + second_number
        elif operation == '-':
            return first_number - second_number
        elif operation == '*':
            return first_number * second_number
        elif operation == '/':
            if second_number != 0:
                return first_number / second_number
            else:
                print("Ошибка: деление на ноль!")
                return None
        else:
            print("Некорректная операция.")
            return None
