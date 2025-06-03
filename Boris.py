from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index Page')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user', defaults={"username": "John Smith"})
@app.route('/user/', defaults={"username": "John Smith"})
@app.route('/user/<username>')
def hello_username(username=None):
    return f"Hello {username}"


@app.route('/form', methods=['GET', 'POST'])
def form():
    html = """
    <form method='post'>
        Name: <input type="text" name="name"></input>
        <input type="submit">
    </form>
    """
    if request.method == 'GET':
        return html

    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('form'))