from flask import Flask, render_template, request
from interview import Interview
import tempfile

app = Flask(__name__)

job_listing = "Please submit a job listing below."


@app.route("/", methods=["GET", "POST"])
def index(job_listing=job_listing):
    if request.method == "POST":
        job_listing = request.form.get("listing")
        jd_submitted = True
    else:
        jd_submitted = False
    return render_template("base.html", listing=job_listing, jd_submitted=jd_submitted)

@app.route("/interview", methods = ["POST"])
def interview(job_listing=job_listing):
    jd_filename = tempfile.mktemp(prefix='job_desc_', suffix='.txt', dir = 'ignore')
    with open (jd_filename, 'w') as file:
        file.write(job_listing)
    Interview(jd_filename)
    return render_template("interview.html", listing=job_listing)