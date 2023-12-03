from flask import Flask
app = Flask(__name__) 

names = {'Max': [18, 'tester'], 'Nik': [27, 'bloger']}

@app.route('/users/<name>')
def users(name):
    user = names[name]
    return user

if   __name__	== "__main__":
    app.run()
