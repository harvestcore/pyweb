from flask import *

app = Flask(__name__)

def notFound():
    return render_template('notfound.html')

@app.route('/')
def inicio():
    return render_template('main.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/ipcontainer')
def ipcontainer():
    return render_template('ipcontainer.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/repositorios')
def repositorios():
    return render_template('repositorios.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def nf(a):
    return notFound()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
