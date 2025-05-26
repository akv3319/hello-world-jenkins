from flask import Flask
from hello import say_hello

app = Flask(__name__)

@app.route('/')
def home():
    return say_hello()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
