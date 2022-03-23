from flask import Flask, request, redirect, url_for, render_template
import smtplib, ssl

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST') )
def home():
    if request.method == 'POST':
        name = request.form['name']
        tel = request.form['tel']
        email = request.form['email']
        msg = request.form['msg']

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "video181881@gmail.com"
        receiver_email = "lucas-camargo@outlook.com"
        key = f"{os.getenv("MAIL_KEY")}"
        message = f"""\
Subject: MENSAGEM DO SITE
{name}, {tel}, {email}
{msg} ."""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, key)
            server.sendmail(sender_email, receiver_email, message)

        return redirect(url_for('home'))

    return render_template('home.html')