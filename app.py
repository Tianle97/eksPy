"""
Imports the Flask web framework, which is used to build web applications in Python.
"""
from flask import Flask

# If the import is still not resolved, you may need to install Flask:
# pip install flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a simple Flask application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)