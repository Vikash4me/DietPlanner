from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    bmi = db.relationship('BMI', backref='user')
    fitness_goal = db.relationship('Fitness_goal', backref='user')
    water_track = db.relationship('Water_track', backref='user')
    macros = db.relationship('Macros', backref='user')
    #budget = db.relationship('Plan_acc_budget', backref='user')