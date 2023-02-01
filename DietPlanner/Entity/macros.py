from config import db

class Macros(db.Model):
    __tablename__ = 'macros'
    id= db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    protein = db.Column(db.String(200), nullable=False)
    carbs = db.Column(db.String(200), nullable=False)
    fats = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user_email = db.Column(db.Integer, db.ForeignKey("user.email"))