from flask import *
from flask_bootstrap import *

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
