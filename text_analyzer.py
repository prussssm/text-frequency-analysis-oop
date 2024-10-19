import random
import string

class TextAnalyzer:
    def __init__(self):
        self.text = ""
        self.frequency = {}

    def input_data(self):
        choice = input("Выберите способ ввода (1 - вручную, 2 - случайно): ")
        if choice == '1':
            self.text = input("Введите текст: ")
        elif choice == '2':
            length = int(input("Введите длину случайного текста: "))
            self.text = ''.join(random.choices(string.ascii_letters + string.punctuation + ' ', k=length))
        else:
            print("Неверный выбор!")

    def execute_algorithm(self):
        if not self.text:
            print("Сначала введите данные!")
            return
        
        total_chars = len(self.text)
        self.frequency = {}
        for char in self.text:
            self.frequency[char] = self.frequency.get(char, 0) + 1
        
        for char in self.frequency:
            self.frequency[char] /= total_chars

    def output_result(self):
        if not self.frequency:
            print("Сначала выполните алгоритм!")
            return
        
        for char, freq in self.frequency.items():
            print(f"'{char}': {freq:.4f}")

    def validate_input(self):
        pass

class Menu:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def display(self):
        print("\nМеню:")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы")

    def handle_choice(self):
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            self.analyzer.input_data()
        elif choice == '2':
            self.analyzer.execute_algorithm()
        elif choice == '3':
            self.analyzer.output_result()
        elif choice == '4':
            return False
        else:
            print("Неверный выбор!")
        return True

    def run(self):
        pass

def main():
    analyzer = TextAnalyzer()
    menu = Menu(analyzer)
    
    while True:
        menu.display()
        if not menu.handle_choice():
            break

if __name__ == "__main__":
    main()