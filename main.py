import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify

my_email = os.getenv("FROM_EMAIL", "")
my_password = os.getenv("FROM_EMAIL_PASSWORD", "")
send_to_email = os.getenv("TO_EMAIL", "")
smtp_server = os.getenv("SMTP_SERVER", "")
smtp_port = os.getenv("SMTP_PORT", 465)

app = Flask(__name__)

subject = 'New SMS'

@app.route('/', methods=['POST', 'GET'])
def process():
    data = request.form.get("data")
    msg = MIMEMultipart()
    msg["From"] = my_email
    msg["To"] = send_to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(data, 'plain'))

    server = smtplib.SMTP_SSL('smtp.qq.com', smtp_port)
    server.ehlo()
    server.login(my_email, my_password)
    server.sendmail(my_email, send_to_email, msg.as_string())
    server.quit()
    return msg.as_string()
if __name__ == '__main__':
    port = os.getenv('PORT', default=5000)
    app.run(host='0.0.0.0', port=port)
