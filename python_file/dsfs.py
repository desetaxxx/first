from flask import *
app = Flask(__name__)  


@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/about')
def about():
    return 'О нас'


@app.route('/downloads')
def downloads():
    return 'Загрузки'


if   __name__	== "__main__":
    app.run()
    

