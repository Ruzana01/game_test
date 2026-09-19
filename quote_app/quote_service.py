import random

class QuoteService:
    def __init__(self):
        # Готовый список фраз
        self.quotes = [
            "Всё обязательно получится!",
            "Отличный день, чтобы написать хороший код!",
            "Ошибки — это просто опыт, продолжай!",
            "Ты делаешь успехи с каждым днём!",
            "Сделай паузу и выпей чаю"
        ]

    def get_random_quote(self) -> str:
        """Возвращает случайную цитату."""
        return random.choice(self.quotes)

    def add_quote(self, text: str) -> bool:
        """Добавляет новую цитату в список."""
        cleaned_text = text.strip()
        if cleaned_text:
            self.quotes.append(cleaned_text)
            return True
        return False