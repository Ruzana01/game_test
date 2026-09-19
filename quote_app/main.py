import flet as ft
from quote_service import QuoteService

def main(page: ft.Page):
    page.title = "Генератор цитат"
    page.window.width = 500
    page.window.height = 500
    page.padding = 20

    service = QuoteService()

    # Элементы интерфейса
    quote_text = ft.Text(
        value="Нажми на кнопку, чтобы получить цитату!",
        size=16,
        italic=True
    )
    
    input_field = ft.TextField(hint_text="Добавить свою цитату...", expand=True)

    # Логика для кнопок
    def get_click(e):
        quote_text.value = service.get_random_quote()
        page.update()

    def add_click(e):
        if service.add_quote(input_field.value):
            quote_text.value = f"Добавлено: {input_field.value}"
            input_field.value = ""
        else:
            quote_text.value = "Ошибка: нельзя добавить пустую цитату!"
        page.update()

    # Размещение элементов (заменили ElevatedButton на Button)
    page.add(
        quote_text,
        ft.Button("Получить цитату 🎲", on_click=get_click),
        ft.Divider(),
        ft.Row([
            input_field,
            ft.Button("Добавить", on_click=add_click)
        ])
    )

if __name__ == "__main__":
    ft.run(main)