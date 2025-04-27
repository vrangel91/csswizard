from app import db
from datetime import datetime


class Progress(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'), nullable=False)
	completed = db.Column(db.Boolean, default=False)
	user_code = db.Column(db.Text, nullable=True)
	score = db.Column(db.Integer, default=0)
	attempts = db.Column(db.Integer, default=0)
	completed_at = db.Column(db.DateTime, nullable=True)
	last_attempt_at = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return f'<Progress User:{self.user_id} Challenge:{self.challenge_id} Completed:{self.completed}>'