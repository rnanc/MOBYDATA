from flask_mail import Mail, Message
mail = Mail()

def configure(app):
    mail.init_app(app)

def send_message(subject, email, body):
    msg = Message(subject=subject,
                  sender=email,
                  recipients=["elielsonbr.com@gmail.com"],
                  body="from: {}\n\n{}".format(email, body))
    mail.send(msg)




