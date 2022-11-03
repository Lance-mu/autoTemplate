from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# 初始化SQLAlchemy
db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = "roles"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "Role:%s" % self.name


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    avator = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    rs = db.relationship("Report", backref="report", lazy="dynamic")

    def __repr__(self):
        return "User:%s" % self.name


class Report(db.Model):
    __tablename__ = "reports"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)
    look_time = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return "Report:%s" % self.title


if __name__ == '__main__':
    print(datetime.now())