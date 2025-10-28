# models.py
from extensions import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    comment_text = db.Column(db.String(255), nullable=False)
