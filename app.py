from flask import Flask, render_template, request, jsonify
from email.mime.text import MIMEText
import smtplib


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'You have received a new contact'
    msg['From'] = name
    msg['To'] = email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("chtest2021@gmail.com", "Mapping1999")
    server.sendmail("chtest2021@gmail.com", email, msg.as_string())
    return render_template("success.html", name=name, email=email, message=message)
