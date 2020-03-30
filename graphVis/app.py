from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open('graph.json') as json_data:
        d = json.load(json_data)
    print(d)
    return render_template("home.html",data=d)

if __name__ == "__main__":
    app.run(debug=True)