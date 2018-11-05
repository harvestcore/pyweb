from django.shortcuts import render

# Create your views here.

def login():
    addToHistory("login")
    return render_template('login.html')

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

def logout():
    if session.get('username') and session.get('loggedIn'):
        if session['loggedIn']:
            session.pop('username')
            session['loggedIn'] = False
    addToHistory("logout")
    return redirect(url_for('inicio'))

def signup():
    addToHistory("signup")
    return render_template('signup.html')

def signup_post():
    addToHistory("signup")
    user = request.form['username']
    db[user] = {"username":request.form['username'], "password":request.form['password'], "firstname":request.form['firstname'], "lastname":request.form['lastname'], "email":request.form['email'], "telnumber":request.form['telnumber'], "birthdate":request.form['birthdate']}
    return redirect(url_for('login'))

def profile():
    if session.get('loggedIn'):
        if session['loggedIn']:
            return render_template('profile.html')
    else:
        return redirect(url_for('inicio'))

def modifyprofile():
    if session.get('loggedIn'):
        if session['loggedIn']:
            return render_template('modifyprofile.html')
    else:
        return redirect(url_for('inicio'))

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