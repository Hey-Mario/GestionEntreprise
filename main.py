from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
