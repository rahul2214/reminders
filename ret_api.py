import face_recognition
import cv2
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12657369:KSzpGU9blD@sql12.freesqldatabase.com/sql12657369'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database model
class Model(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    task = db.Column(db.String(200))
    date = db.Column(db.Date)

cap = cv2.VideoCapture(0)

@app.route('/')
def face_recognition_api():
    if request.method == 'GET':
        

        image_1 = face_recognition.load_image_file("ref.jpg")     
        face_locations_img_1 = face_recognition.face_locations(image_1)
        if face_locations_img_1:
          face_encodings_img_1 = face_recognition.face_encodings(image_1, face_locations_img_1)
        else :
         print('face not detected')


        image_2 = face_recognition.load_image_file("ref1.jpg")
        face_locations_img_2 = face_recognition.face_locations(image_2)
        if face_locations_img_2:
          face_encodings_img_2 = face_recognition.face_encodings(image_2, face_locations_img_2)
        else :
          print('face not detected')   


        image_3 = face_recognition.load_image_file("ref2.jpg")
        face_locations_img_3 = face_recognition.face_locations(image_3)
        if face_locations_img_3:
          face_encodings_img_3 = face_recognition.face_encodings(image_3, face_locations_img_3)
        else :
          print('face not detected')   


        image_4 = face_recognition.load_image_file("ref3.jpg")
        face_locations_img_4 = face_recognition.face_locations(image_4)
        if face_locations_img_4:
          face_encodings_img_4 = face_recognition.face_encodings(image_4, face_locations_img_4)
        else :
          print('face not detected')


        while True:
          ret, frame = cap.read()
          face_locations_cam = face_recognition.face_locations(frame)

          rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

          if len(face_locations_cam) == 0:
            
            return jsonify({"message": "No faces detected in the frame."})

          else:
            
            face_encodings_cam = face_recognition.face_encodings(rgb_frame)[0]
        

          match_1 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_1)
          match_2 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_2)    
          match_3 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_3)    
          match_4 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_4)    

          if match_1[0]:
            name = "architha"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="architha", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            return render_template('info.html', data=data, name=name, msg=msg)
        
        
          elif match_2[0]:
            name = "Rahul"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="Rahul", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            return render_template('info.html', data=data, name=name, msg=msg)
        

          elif match_3[0]:
            name = "prabhas"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="prabhas", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            return render_template('info.html', data=data, name=name, msg=msg)
        

          elif match_4[0]:
            name = "bhanu"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="bhanu", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            return render_template('info.html', data=data, name=name, msg=msg)

        

          return jsonify({"message": "match found."})


if __name__ == '__main__':
    app.run(port=8080, debug=True)
