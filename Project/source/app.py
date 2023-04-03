from flask import Flask, request, render_template, url_for
from markupsafe import escape

# get css

# flask run --host=0.0.0.0 (to make the server public)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Start Page'

@app.route('/start')
@app.route('/start/<name>')
def startMenu(name=None):
    # start menu
    return render_template('start.html', name=name)

# show the login form
@app.get('/login')
def login_get():
    return 'show login form'

# do the login 
@app.post('/login')
def login_post():
    return 'do the login'

@app.route("/<gadget>")
def gadgetMenu(gadget):
    # Render the page
    return f"{escape(gadget)}"

@app.route("/<profile>")
def profileMenu(profile):
    # Render Page
    return f'{escape(profile)}'

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)