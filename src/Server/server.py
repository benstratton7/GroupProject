from bottle import route, run, static_file, error, get, post, request, template


@error(404)
def error404(error):
    return '4040404040404 ' \
           'file not found!'


'''
@route('/<filename>')
def game(filename):
    return static_file(filename, root="C:/Users/benns/IdeaProjects/GroupProject/src/AndrewsHTMLFiles/")
'''


@route('/')
def mainPage():
    return static_file("mainPage.html", root="C:/Users/benns/IdeaProjects/GroupProject/src/AndrewsHTMLFiles/")


@route('/join')
def login():
    return static_file("LoginPage.html", root="C:/Users/benns/IdeaProjects/GroupProject/src/AndrewsHTMLFiles/")


@get('/players')
def show_users():
    names = ""
    with open("users.txt", "r") as f:
        for line in f:
            names = names + line
    return template("<p> {{names}} </p>", names=names)


@post('/action_page.php')
def join_game():
    with open("users.txt", "a") as f:
        name = request.forms.get('usrnm')
        f.write(("\n" + name))
    return static_file("waitingRoom.html", root="C:/Users/benns/IdeaProjects/GroupProject/src/AndrewsHTMLFiles/")


# @get('/action_page.php')
# def after_login():
#     return static_file("waitingRoom.html", root="C:/Users/benns/IdeaProjects/GroupProject/src/AndrewsHTMLFiles/")


run(host='localhost', port=8080, debug=True)
