from flask import Flask, render_template, request

app = Flask(__name__)

job_listing = "Please submit a job listing below."


@app.route("/", methods=["GET", "POST"])
def index(job_listing=job_listing):
    if request.method == "POST":
        job_listing = request.form.get("listing")
    return render_template("base.html", listing=job_listing)
