# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def to_dict(self):
        """ 将模型转换为字典 """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
# models.py


class Baselines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baseline_name = db.Column(db.String(255), nullable=False)
    baseline_status = db.Column(db.String(50), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """ 将模型转换为字典 """
        return {
            'id': self.id,
            'baseline_name': self.baseline_name,
            'baseline_status': self.baseline_status,
            'owner': self.owner,
            'timestamp': self.timestamp.isoformat()
        }


class Project(db.Model):
    __tablename__ = 'project_1'
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    job_name = db.Column(db.String(100), nullable=False)
    job_num = db.Column(db.Integer, nullable=False)
    job_status = db.Column(db.String(50), nullable=False)
    fail_reason = db.Column(db.Text)
    owner = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """ 将模型转换为字典 """
        return {
            'id': self.id,
            'project_name': self.project_name,
            'job_name': self.job_name,
            'job_num': self.job_num,
            'job_status': self.timestamp.job_status(),
            'fail_reason': self.fail_reason,
            'owner': self.owner,
            'time': self.time
        }