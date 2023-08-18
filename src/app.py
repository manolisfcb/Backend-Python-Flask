from flask import Flask
from flask_restful import Api
from oa import oauth
app = Flask(__name__)
oauth.init_app(app)

api = Api(app)

app.secret_key = 'development'

@app.route('/')
def index():
    return '<a href="/login">Login with GitHub</a>'

from routes.login import Login



api.add_resource(Login, '/login')



if __name__ == '__main__':
    oauth.init_app(app)
    app.run(debug=True)