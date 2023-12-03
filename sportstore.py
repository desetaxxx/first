from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB_athletes1.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))
    sport = db.Column(db.String(50))
    
    def __init__(self, name, gender, age, country, sport):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = country
        self.sport = sport 
        
with app.app_context():
    db.create_all()
    users = User.query.all()
    user = User('Eva', 'female', 29, 'USA', 'hockey')
    db.session.add(user)
    db.session.commit()
    db.session.close()
    print(user)    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/athletes')
def athletes():
    return render_template('athletes.html')

if __name__ == "__main__":
    app.run()


