from flask import Flask, render_template, redirect, flash, session, request
import jinja2
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "it's_a_secret"

app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index_page():
    """Show an index page."""

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Displays a job application form."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_submission():
    """Submits job application form."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_req = request.form.get("salaryreq")
    job_title = request.form.get("jobtitle")

    return render_template("application-response.html", 
                            firstname=first_name, 
                            lastname=last_name, 
                            salaryreq=salary_req, 
                            jobtitle=job_title)





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

