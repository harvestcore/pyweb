from flask import *
from pickleshare import *
import json
from db import *
import requests

app = Flask(__name__)
app.secret_key = 'Yxpn7caLHKDLiFuJHz2H'

db = PickleShareDB('pickledb')
# db.clear()
history = ["", "", ""]

# def getIntervalos(items, div):
#     intervalos = []
#     intervalos2 = []
#     nointv = int(items / div)
#     index = 1

#     for i in range(nointv+1):
#         intmin = i * div
#         intmax = (index*div)-1
#         if intmax > items:
#             intmax = items
#         intervalos.append({'min':intmin, 'max':intmax})
#         index += 1
#         intervalos2.append(i)

#     return {'values':intervalos, 'valuesindex':intervalos2}


def notFound():
    return render_template('notfound.html')

def addToHistory(page):
    history.insert(0, page)
    if len(history) == 4:
        history.pop(3)

    session['history'] = history

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
    repos = requests.get('https://api.github.com/users/harvestcore/repos').json()
    clean_repos = []

    for i in range(len(repos)):
        clean_repos.append({
            'name':repos[i]['name'],
            'description':repos[i]['description'],
            'url':repos[i]['html_url'],
            'updated_at':repos[i]['updated_at'],
            'stars':repos[i]['stargazers_count'],
            'forks':repos[i]['forks'],
            'license':repos[i]['license'],
            'language':repos[i]['language'],
            'is_fork':repos[i]['fork']
        })

    session['repos'] = clean_repos

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
    if session.get('username') and session.get('loggedIn'):
        if session['loggedIn']:
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
    if session.get('loggedIn'):
        if session['loggedIn']:
            return render_template('profile.html')
    else:
        return redirect(url_for('inicio'))

@app.route('/modifyprofile')
def modifyprofile():
    if session.get('loggedIn'):
        if session['loggedIn']:
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
    session['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
    
    addToHistory("restaurantes")
    return render_template('restaurantes.html')

@app.route('/restaurantes', methods=['POST'])
def restaurantes_post():
    ##  Update de datos
    # try:
    #     mod_rest_name = request.form['rest_name']
    #     mod_rest_coord = request.form['rest_coord']
    #     mod_rest_type = request.form['rest_type']
        
    #     if mod_rest_name != session['current_rest']['name'] or mod_rest_coord != session['current_rest']['coordinates'] or mod_rest_type != session['current_rest']['type']:
    #         Restaurantes.findAndUpdate(session['current_rest']['id'], {'name':mod_rest_name})
    #         Restaurantes.findAndUpdate(session['current_rest']['id'], {'location':{'coordinates':mod_rest_coord, 'type':session['current_rest']['type']}})
    #         Restaurantes.findAndUpdate(session['current_rest']['id'], {'location':{'coordinates':session['current_rest']['coordinates'], 'type':mod_rest_type}})
    #         session['current_rest'] = {'name':mod_rest_name, 'id':session['current_rest']['id'], 'coordinates':mod_rest_coord, 'type':mod_rest_type}
    # except:
    #     mod_rest_name = session['current_rest']['name']
    #     mod_rest_coord = session['current_rest']['coordinates']
    #     mod_rest_type = session['current_rest']['type']
    #     session['current_rest'] = {'name':mod_rest_name, 'id':session['current_rest']['id'], 'coordinates':mod_rest_coord, 'type':mod_rest_type}

    ## Búsqueda por nombre
    try:
        srchname = request.form['search_by_name']
        rest = Restaurantes.getListByName(srchname)
        session['lista_rest'] = rest
        
    except:
        srchname = None
    
    # Búsqueda por ID
    try:
        srchid = request.form['search_by_id']
        rest = Restaurantes.getByID(srchid)
        session['lista_rest'] = rest
    except:
        srchid = None

    # ## Borrado por nombre
    # try:
    #     delname = request.form['del_by_name']
    #     rest = Restaurantes.delByName(delname)
    #     session['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
    # except:
    #     srchname = None
    
    # ## Borrado por ID
    # try:
    #     delid = request.form['del_by_id']
    #     rest = Restaurantes.delByID(delid)
    #     session['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
    # except:
    #     delid = None

    # ##  Agregar restaurante
    # try:
    #     add_rest_name = request.form['add_name']
    #     add_rest_coord = request.form['add_coord']
    #     add_rest_type = request.form['add_type']

    #     Restaurantes.add(add_rest_name, add_rest_coord, add_rest_type)
    # except:
    #     add_rest_name = None
    #     add_rest_coord = None
    #     add_rest_type = None

    addToHistory("restaurantes")
    return render_template('restaurantes.html')

@app.errorhandler(404)
def nf(a):
    return notFound()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
