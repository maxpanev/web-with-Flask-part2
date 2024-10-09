from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
   # Получаем текущие дату и время
   now = datetime.now()
   # Форматируем дату и время в удобочитаемый формат
   formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
   # Возвращаем их в качестве ответа
   return f"<h1>Текущие дата и время: {formatted_time}</h1>"

if __name__ == "__main__":
    app.run()