from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def fecha_actual():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Bienvenido a credibanco web. La Hora actual es: {current_time}'

if __name__ == '__main__':
    app.run(debug=True)
