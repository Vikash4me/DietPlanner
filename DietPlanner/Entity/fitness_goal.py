from config import db

class Fitness_goal(db.Model):
    __tablename__ = 'fitness_goal'
    id = db.Column(db.Integer, primary_key=True)
   # email = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    fat_loss= db.Column(db.String(200), nullable=False)
    weight_gain = db.Column(db.String(200), nullable=False)
    muscle_building = db.Column(db.String(200), nullable=False)
    steps_counter = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user_email = db.Column(db.Integer, db.ForeignKey("user.email"))