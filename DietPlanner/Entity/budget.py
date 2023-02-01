from config import db

class Plan_acc_budget(db.Model):
    __tablename__ = 'budget'
    username = db.Column(db.String, primary_key=True)

    plans = db.Column(db.String(200), nullable=False)
    user_name = db.Column(db.String, db.ForeignKey("user.username"))