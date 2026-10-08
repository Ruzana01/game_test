import pytest

# Исходная функция из задания
def get_result(score, attendance):
    if not isinstance(score, (int, float)):
        raise TypeError("Баллы должны быть числом")

    if not isinstance(attendance, (int, float)):
        raise TypeError("Посещаемость должна быть числом")

    if score < 0 or score > 100:
        return "Некорректный балл"

    if attendance < 0 or attendance > 100:
        return "Некорректная посещаемость"

    if score >= 90 and attendance >= 80:
        return "Отлично"

    if score >= 70 and attendance >= 70:
        return "Хорошо"

    if score >= 50 and attendance >= 60:
        return "Зачёт"

    return "Незачёт"


# ==========================================
# АВТОМАТИЗИРОВАННЫЕ ТЕСТЫ (Pytest)
# ==========================================

# 1. Проверка классов эквивалентности и граничных значений
@pytest.mark.parametrize("score, attendance, expected_result", [
    # Успешные границы и стандартные случаи
    (90, 80, "Отлично"),
    (100, 100, "Отлично"),
    (70, 70, "Хорошо"),
    (89, 79, "Хорошо"),
    (50, 60, "Зачёт"),
    (69, 69, "Зачёт"),
    (49, 100, "Незачёт"),
    (100, 59, "Незачёт"),
    (0, 0, "Незачёт"),
    
    # Некорректные значения (выход за границы 0-100)
    (-1, 80, "Некорректный балл"),
    (101, 80, "Некорректный балл"),
    (80, -1, "Некорректная посещаемость"),
    (80, 101, "Некорректная посещаемость"),
])
def test_get_result_logic(score, attendance, expected_result):
    assert get_result(score, attendance) == expected_result


# 2. Проверка типов данных (перехват TypeError через pytest.raises)
@pytest.mark.parametrize("score, attendance", [
    ("90", 80),     # Строка в score
    (90, "80"),     # Строка в attendance
    (None, 80),     # None в score
    (90, [80]),     # Список в attendance
])
def test_get_result_invalid_types(score, attendance):
    with pytest.raises(TypeError):
        get_result(score, attendance)