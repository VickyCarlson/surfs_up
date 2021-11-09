from flask import Flask
# create new Flask app instance
app = Flask(__name__)
#create a route
@app.route('/')
def hello_world():
    return 'Hello world'