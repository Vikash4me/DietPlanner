from config import db

class Water_track(db.Model):
    __tablename__ = 'water_track'

    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    water_intake = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user_email = db.Column(db.Integer, db.ForeignKey("user.email"))
