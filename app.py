from flask import Flask
from markupsafe import escape

from flask import url_for
from flask import request
from flask import render_template


# url_for('static', filename='style.css')

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p> <a href='/index'>Indonesia</a>"

# @app.route("/index")
# def hello():
#     return "<p>Halo, Dunia!</p>  <a href='/'>Inggris</a>"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

@app.route('/')
def index():
    login = url_for('login')
    load_image = url_for('static', filename='img/Mang.jpg')
    return f'<a href="{login}">Click Me</a><br><a href="{ url_for("login") }">Click Me 2</a><br><img src="{load_image}">'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
    
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()



@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



#DELETE
# Sample data
resources = {
    '1': 'Resource 1',
    '2': 'Resource 2',
    # ... other resources
}

@app.delete('/resource/<resource_id>')
def delete_resource(resource_id):
    if request.method == 'DELETE':
        if resource_id in resources:
            del resources[resource_id]
            return f'Resource {resource_id} deleted', 200
        else:
            return f'Resource {resource_id} not found', 404
        

#PUT
@app.route('/update', methods=['PUT'])
def update_resource():
    if request.method == 'PUT':
        # Handle the PUT request here
        # Access the request data using request.data or request.get_data()
        data = request.data
        # Process and update the resource

        return f'Updated resource with data: {data}', 200
    
    
#GET
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'