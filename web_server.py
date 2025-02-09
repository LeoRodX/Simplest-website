from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Мой простой сайт</title>
        </head>
        <body>
            <h1>Добро пожаловать на мой сайт!</h1>
            <p>Это простой веб-сайта, созданного для отладки приложения проверки доступности 
            сайтов.</p>
        </body>
        </html>
    ''')


if __name__ == '__main__':
    app.run(debug=False)