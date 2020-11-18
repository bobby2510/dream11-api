import flask
import json
app = flask.Flask(__name__)

@app.route('/',methods=['GET',])
def home():
    f = open('data.json')
    result = json.load(f)
    return result 


if __name__ == "__main__":
    app.run()