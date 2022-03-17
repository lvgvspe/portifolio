from flask import Flask, request, redirect, url_for, render_template
import smtplib, ssl

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST') )
def inicio():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        msg = request.form['msg']

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "video181881@gmail.com"
        receiver_email = "lucas-camargo@outlook.com"
        chave = "hloqihtnohnsiycb"
        message = f"""\
Subject: MENSAGEM DO SITE
{name}, {phone}, {email}
{msg} ."""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, chave)
            server.sendmail(sender_email, receiver_email, message)

        return redirect(url_for('inicio'))

    return render_template('inicio.html')