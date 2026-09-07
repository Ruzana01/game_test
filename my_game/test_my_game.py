import pytest
from my_game.game_logic import BunkerGame

# 1. ПОЗИТИВНЫЕ ТЕСТЫ (Проверка корректной работы)

def test_initial_state():
    """Проверяем начальное состояние игры."""
    game = BunkerGame()
    assert game.oxygen == 10
    assert game.has_keycard is False
    assert game.is_game_over is False

def test_find_keycard():
    """Проверяем, что действие '1' выдает ключ-карту."""
    game = BunkerGame()
    message = game.make_move("1")
    
    assert game.has_keycard is True
    assert game.oxygen == 9
    assert "нашли ключ-карту" in message

def test_successful_win_scenario():
    """Проверяем полный сценарий победы."""
    # Передаем фиксированный код "1234" для точности теста
    game = BunkerGame(correct_code="1234")
    
    game.make_move("1")                               # Находим карту
    game.make_move("2")                               # Смотрим код
    message = game.make_move("3", user_code="1234")   # Вводим верный код
    
    assert game.is_won is True
    assert game.is_game_over is True
    assert game.oxygen == 7
    assert "ПОБЕДА" in message


# 2. НЕГАТИВНЫЕ ТЕСТЫ (Проверка ошибок и крайних случаев)

def test_invalid_choice_input():
    """Проверяем ввод некорректной команды (буквы)."""
    game = BunkerGame()
    message = game.make_move("abc")
    
    assert game.oxygen == 9  # Ход все равно потратился
    assert "Неверная команда" in message

def test_wrong_security_code():
    """Проверяем ввод неверного кода."""
    game = BunkerGame(correct_code="7777")
    game.make_move("1")  # Берем карту
    
    message = game.make_move("3", user_code="0000")  # Ошибка в коде
    
    assert game.is_won is False
    assert "НЕВЕРНЫЙ КОД" in message

def test_game_over_when_oxygen_runs_out():
    """Проверяем поражение, если закончился кислород."""
    game = BunkerGame()
    
    # Тратим все 10 ходов
    for _ in range(10):
        game.make_move("4")
        
    assert game.oxygen == 0
    assert game.is_game_over is True
    assert game.is_won is False