import textakel

from flask import Flask
from flask import jsonify
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/<string:function_name>/<path:s>")
def get_text(function_name, s):
    s = textakel.takel(function_name, s)
    response = {"text": s}
    return jsonify(response)


@app.route("/api")
def get_functions():
    functions_names = textakel.get_functions()
    response = {"functions": functions_names}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
