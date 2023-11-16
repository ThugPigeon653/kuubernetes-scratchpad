# A placeholder application, to prove functionality of the repository. 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Response MULTICONTAINER Flask application"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')