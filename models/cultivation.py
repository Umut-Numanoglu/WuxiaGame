from datetime import datetime

from game import db


class Cultivation(db.Model):
    __tablename__ = "cultivation"

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    cultivation_type = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
