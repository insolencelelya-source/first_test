# UI Automation Test (Playwright + Python)

Тест проверяет пользовательский сценарий доната.

## Сценарий
1. Открывается страница
2. Нажимается кнопка "Click me"
3. Открывается виджет доната
4. Нажимается "Give Now"
5. Выбирается режим "Monthly"
6. Вводится сумма 5000
7. Нажимается кнопка Donate
8. Проверяется переход на форму "Enter your details"

## Технологии
- Python
- Playwright
- Pytest

## Запуск

```bash
pip install -r requirements.txt
pytest --headed -s
