from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha512
db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    company_name = db.Column(db.String(200), nullable=False)
    cam_ref = db.Column(db.String(200), nullable=True)
    provider = db.Column(db.String(200), nullable=False)
    reports = db.relationship("Report", backref='users', lazy="select")
    def gen_hash(self):
        self.password = pbkdf2_sha512.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha512.verify(password, self.password)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200))
    date = db.Column(db.String(200))
    report_type = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))





