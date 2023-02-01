from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
from Entity.user import User
from Entity.bmi import BMI
from Entity.macros import Macros
from Entity.fitness_goal import Fitness_goal  
from Entity.water_track import Water_track

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATINS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        
        @app.route('/signup', methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)

            user = User.query.filter_by(username=data['username']).first()

            if user is None:
                new_user = User(
                    username = data['username'],
                    password = data['password'],
                    email = data['email']
                )

                db.session.add(new_user)
                db.session.commit()
                return jsonify(msg = "user signup is done successfully")
            else:
                return jsonify(msg="User already exists")
        
        @app.route('/water_checker', methods = ['POST'])
        def water_checker():
            rec_username= request.args.get('username')
            user = User.query.filter_by(username=rec_username).first()
            print(user.username)
            waterchecker = request.get_json()

            new_water = Water_track(
                username = waterchecker["waterchecker"]['username'],
                water_intake= waterchecker["waterchecker"]["water_intake"],
                user_id= user.id
            )
            db.session.add(new_water)
            db.session.commit()
            print(new_water)
            return jsonify(msg="we recieved your water details, but for normal functioning please have 8 glasses of water")
        
        @app.route('/bmi_details', methods = ['POST'])
        def calculate_bmi():
            username= request.args.get('username')
            user = User.query.filter_by(username=username).first()
            #data = request.form.to_dict(flat=True)
            data = request.get_json()
            # user = User.query.filter_by(username=data['username']).first()

            details = BMI(
                username = data['username'],
                height = data['height'],
                weight = data['weight'],
                user_id = user.id
            )

            
            db.session.add(details)
            db.session.commit()
            print(details)
            return jsonify(msg="details submitted successfully")

        # @app.route('/login', methods=['POST'])
        # def login():
        #     recv_username = request.args.get('username')
        #     recv_password = request.args.get('password')
        #     user = User.query.filter(username=recv_username).first()
        #     user = User.query.filter(password = recv_password).first()
        # db.drop_all()
        db.create_all()
        db.session.commit()

        return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)