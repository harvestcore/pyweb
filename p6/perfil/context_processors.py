usr = {
    'username': '',
    'email': '',
    'firstname': '',
    'lastname': '',
    'birthdate': '',
    'telnumber': '',
    'loggedin': False
}

def current_user(request):
    if 'current_user' not in request.session:
        return { 'current_user': usr}
    else:
        return { 'current_user': request.session.get('current_user') }