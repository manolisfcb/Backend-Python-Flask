from flask import Flask
from flask_restful import Api

app = Flask(__name__)


api = Api(app)

app.secret_key = 'development'

@app.route('/')
def index():
    return '<a href="/login">Login with GitHub</a>'



if __name__ == '__main__':
    app.run(debug=True)