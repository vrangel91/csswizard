from app import db


class Challenge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	level = db.Column(db.Integer, nullable=False)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text, nullable=False)
	instructions = db.Column(db.Text, nullable=False)
	starter_code = db.Column(db.Text, nullable=False)
	solution_code = db.Column(db.Text, nullable=False)
	success_criteria = db.Column(db.Text, nullable=False)
	hint = db.Column(db.Text, nullable=True)
	max_score = db.Column(db.Integer, default=100)
	css_property_focus = db.Column(db.String(100), nullable=False)
	css_effect_category = db.Column(db.String(50), nullable=False)  # animation, transition, transform, etc.
	difficulty = db.Column(db.String(20), nullable=False)  # easy, medium, hard



	# Relacionamento com o progresso
	progress_entries = db.relationship('Progress', backref='challenge', lazy=True)



	def __repr__(self):
		return f'<Challenge {self.title} (Level {self.level})>'