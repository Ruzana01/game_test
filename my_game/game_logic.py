import random

class BunkerGame:
    def __init__(self, oxygen=10, correct_code=None):
        self.oxygen = oxygen
        self.has_keycard = False
        # Если код не передан (например, в тесте), генерируем случайный 4-значный
        self.correct_code = correct_code if correct_code else str(random.randint(1000, 9999))
        self.searched_desk = False
        self.searched_safe = False
        self.is_game_over = False
        self.is_won = False
        

    def make_move(self, choice, user_code=None):
        """Выполняет один ход и возвращает текст ответа."""
        if self.is_game_over:
            return "Игра уже окончена."

        # Каждый ход снижает кислород
        self.oxygen -= 1

        # Логика выборов
        if choice == "1":
            if not self.searched_desk:
                self.has_keycard = True
                self.searched_desk = True
                result = "Вы нашли ключ-карту!"
            else:
                result = "Стол пуст."

        elif choice == "2":
            if self.has_keycard:
                self.searched_safe = True
                result = f"Сейф открыт! Код: {self.correct_code}"
            else:
                result = "Сейф заперт. Нужна ключ-карта."

        elif choice == "3":
            if not self.has_keycard:
                result = "Терминал заблокирован. Нужна ключ-карта."
            else:
                if user_code == self.correct_code:
                    self.is_won = True
                    self.is_game_over = True
                    result = "ПОБЕДА! Дверь открыта."
                else:
                    result = "НЕВЕРНЫЙ КОД!"

        elif choice == "4":
            result = f"Инвентарь: Карта={'Есть' if self.has_keycard else 'Нет'}"

        else:
            result = "Неверная команда!"

        # Проверка на окончание кислорода
        if self.oxygen <= 0 and not self.is_won:
            self.is_game_over = True
            result += " Кислород закончился! ПОРАЖЕНИЕ."

        return result