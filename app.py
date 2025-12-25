from flask import Flask
import yaml

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Vulnerable World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
