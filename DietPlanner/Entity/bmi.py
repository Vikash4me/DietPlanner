from config import db

class BMI(db.Model):
    __tablename__ = 'bmi'
    id = db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    # how to get bmi
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #user_email = db.Column(db.Integer, db.ForeignKey("user.email")) 

#     def calculate_bmi(height, weight):
#           return (weight/(height*height))
        
#     print("Your BMI is: ", calculate_bmi(height, weight))


