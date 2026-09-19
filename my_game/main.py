# import random

# def start_game():
#     print("=" * 50)
#     print(" МИССИЯ: ПОБЕГ ИЗ БУНКЕРА")
#     print(" Вы очнулись в запертом бункере.")
#     print(" Запас кислорода ограничен: у вас есть ровно 10 ходов!")
#     print("=" * 50)

#     # Инициализация переменных (Состояние игры)
#     oxygen = 10
#     has_keycard = False
#     correct_code = str(random.randint(1000, 9999))  # Случайный 4-значный код
#     searched_desk = False
#     searched_safe = False

#     while oxygen > 0:
#         print(f"\n[Осталось кислорода (ходов): {oxygen}]")
#         print("Выберите действие:")
#         print("1. Осмотреть письменный стол")
#         print("2. Осмотреть сейф на стене")
#         print("3. Подойти к терминалу выхода")
#         print("4. Проверить инвентарь")
        
#         choice = input("Введите номер действия (1-4): ").strip()

#         # Ход засчитывается при любом действии
#         oxygen -= 1

#         if choice == "1":
#             if not searched_desk:
#                 print("-> Вы обыскали стол и нашли ключ-карту доступа!")
#                 has_keycard = True
#                 searched_desk = True
#             else:
#                 print("-> На столе больше ничего нет, только старые бумаги.")

#         elif choice == "2":
#             if not searched_safe:
#                 if has_keycard:
#                     print(f"-> Вы приложили ключ-карту к сейфу! На столетии загорелась надпись с кодом: {correct_code}")
#                     searched_safe = True
#                 else:
#                     print("-> Сейф заперт. Нужна ключ-карта, чтобы активировать его экран.")
#             else:
#                 print(f"-> Сейф уже открыт. На нем записан код: {correct_code}")

#         elif choice == "3":
#             print("-> Вы подошли к терминалу двери выхода.")
#             if not has_keycard:
#                 print("-> Терминал заблокирован. Сначала нужно активировать систему ключ-картой.")
#             else:
#                 user_code = input("-> Введите 4-значный код безопасности: ").strip()
#                 if user_code == correct_code:
#                     print("\n" + "=" * 50)
#                     print(f" ПОБЕДА! Дверь открыта! Вы успели сбежать, оставив {oxygen} ходов в запасе.")
#                     print("=" * 50)
#                     return
#                 else:
#                     print("-> НЕВЕРНЫЙ КОД! Включилась сирена тревоги.")

#         elif choice == "4":
#             print("-> Ваше состояние:")
#             print(f"   Ключ-карта: {'Есть' if has_keycard else 'Отсутствует'}")
#             print(f"   Код от двери: {correct_code if searched_safe else 'Неизвестен'}")

#         else:
#             print("-> Ошибка: Неверная команда! Вы потеряли время и кислород на суету.")

#     # Если цикл закончился и oxygen == 0
#     print("\n" + "=" * 50)
#     print(" ПОРАЖЕНИЕ! Кислород закончился. Вы потеряли сознание...")
#     print("=" * 50)

# if __name__ == "__main__":
#     start_game()




from game_logic import BunkerGame

def main():
    game = BunkerGame()
    print("=" * 40)
    print(" МИССИЯ: ПОБЕГ ИЗ БУНКЕРА")
    print(" У вас есть 10 ходов (кислород).")
    print("=" * 40)

    while not game.is_game_over:
        print(f"\n[Осталось кислорода: {game.oxygen}]")
        print("1. Осмотреть стол")
        print("2. Осмотреть сейф")
        print("3. Ввести код на терминале")
        print("4. Проверить инвентарь")
        
        choice = input("Выберите действие (1-4): ").strip()

        # Если игрок выбрал терминал и у него есть карта — просим код
        code_input = None
        if choice == "3" and game.has_keycard:
            code_input = input("Введите 4-значный код от двери: ").strip()

        # Вызываем логику
        message = game.make_move(choice, user_code=code_input)
        print(f"-> {message}")

if __name__ == "__main__":
    main()
    