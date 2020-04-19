from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Testing Text2"

if __name__ == "__main__":
    app.run()