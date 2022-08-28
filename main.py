from flask import *
from werkzeug.utils import secure_filename
import calendar

calendar = calendar.HTMLCalendar(firstweekday=0).formatmonth(2022, 8)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", calendar=calendar)


if __name__ == "__main__":
    app.run(debug=True)
