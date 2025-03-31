from calculator import Calculator
def main():
    print("Калькулятор готов к работе.")
    calc = Calculator()
    while True:
        calc.read_input()
if __name__ == "__main__":
    main()
