from flask import *
from pickleshare import *
import json
from db import *

app = Flask(__name__)
app.secret_key = 'Yxpn7caLHKDLiFuJHz2H'

db = PickleShareDB('pickledb')
# db.clear()
history = ["", "", ""]

def notFound():
    return render_template('notfound.html')

def addToHistory(page):
    history.insert(0, page)
    if len(history) == 4:
        history.pop(3)

    session['history'] = history

def getIntervalos(items, div):
    intervalos = []
    nointv = int(items / div)
    index = 1

    for i in range(nointv+1):
        intmin = i * div
        intmax = (index*div)-1
        if intmax > items:
            intmax = items
        intervalos.append({'min':intmin, 'max':intmax})
        index += 1

    return intervalos


@app.route('/')
def inicio():
    addToHistory("inicio")
    return render_template('main.html')

@app.route('/contacto')
def contacto():
    addToHistory("contacto")
    return render_template('contacto.html')

@app.route('/ipcontainer')
def ipcontainer():
    addToHistory("ipcontainer")
    return render_template('ipcontainer.html')

@app.route('/proyectos')
def proyectos():
    addToHistory("proyectos")
    return render_template('proyectos.html')

@app.route('/repositorios')
def repositorios():
    addToHistory("repositorios")
    return render_template('repositorios.html')

@app.route('/login')
def login():
    addToHistory("login")
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    addToHistory("login")
    user = request.form['username']
    passwd = request.form['password']
    if user in db.keys():
        data = db[user]
        if data['password'] == passwd:
            session['username'] = user
            session['password'] = passwd
            session['loggedIn'] = True
            session['data'] = data
            return redirect(url_for('inicio'))
    else:
        return redirect(url_for('signup'))

@app.route('/logout')
def logout():
    if session.get('username') and session['loggedIn']:
        session.pop('username')
        session['loggedIn'] = False
    addToHistory("logout")
    return redirect(url_for('inicio'))

@app.route('/signup')
def signup():
    addToHistory("signup")
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    addToHistory("signup")
    user = request.form['username']
    db[user] = {"username":request.form['username'], "password":request.form['password'], "firstname":request.form['firstname'], "lastname":request.form['lastname'], "email":request.form['email'], "telnumber":request.form['telnumber'], "birthdate":request.form['birthdate']}
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if session.get('loggedin'):
        if session['loggedin']:
            return render_template('profile.html')
    else:
        return redirect(url_for('inicio'))

@app.route('/modifyprofile')
def modifyprofile():
    if session.get('loggedin'):
        if session['loggedin']:
            return render_template('modifyprofile.html')
    else:
        return redirect(url_for('inicio'))

@app.route('/modifyprofile', methods=['POST'])
def modifyprofile_post():
    addToHistory("profile")
    actualUser = session['data']['username']
    newUser = request.form['username']
    db[newUser] = {"username":request.form['username'], "password":request.form['password'], "firstname":request.form['firstname'], "lastname":request.form['lastname'], "email":request.form['email'], "telnumber":request.form['telnumber'], "birthdate":request.form['birthdate']}
    if actualUser != newUser:
        db.pop(actualUser)
        session['data'] = db[newUser]
        return redirect(url_for('logout'))
    else:
        session['data'] = db[newUser]
        return redirect(url_for('modifyprofile'))

@app.route('/restaurantes', methods=['GET'])
def restaurantes():
    session['intervalvalue'] = 100
    items = DBRestaurantes.size()
    session['restsize'] = items
    intervalos = getIntervalos(items, session['intervalvalue'])
    session['intervalos'] = intervalos
    session['lenintervalos'] = len(session['intervalos'])

    session['restaurantes'] = DBRestaurantes.getIntervalo(0, session['intervalvalue'])
    return render_template('restaurantes.html')

@app.route('/restaurantes', methods=['POST'])
def restaurantes_post():
    session['lenintervalos'] = len(session['intervalos'])
    newinterval_value = 0
    intstring = 'intervalo_'
    # intvalue = session['intervalvalue']

    for i in range(len(session['intervalos'])):
        intstring += str(i)
        if intstring in request.files:
            newinterval_value = i
            break
        intstring = 'intervalo_'

    session['restaurantes'] = DBRestaurantes.getIntervalo(newinterval_value * 100, ((newinterval_value+1) * 100) - 1 )
    return render_template('restaurantes.html')

@app.errorhandler(404)
def nf(a):
    return notFound()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
