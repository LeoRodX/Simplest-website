from flask import Flask
from datetime import datetime, time

app = Flask(__name__)

# Функция для проверки, работает ли сайт в текущее время
def is_working_hours():
    now = datetime.now().time()
    start_time = time(9, 0)  # 9:00
    end_time = time(18, 0)   # 18:00
    return start_time <= now <= end_time

@app.route('/')
def home():
    if is_working_hours():
        return "Добро пожаловать на сайт! Мы работаем."
    else:
        return "Сайт не работает. Приходите с 9:00 до 18:00."

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Запуск на порту 8080