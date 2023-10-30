
import mysql.connector 
from flask import Flask, render_template, request , redirect, url_for
import face_recognition
import cv2
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12657369:KSzpGU9blD@sql12.freesqldatabase.com/sql12657369'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



class Model(db.Model):
    __tablename__ = 'task'  # Replace with your table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    task = db.Column(db.String(200))
    date = db.Column(db.Date)

cap = cv2.VideoCapture(0)



@app.route('/')
def index():
    
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
             # No faces detected in the frame, handle this case as needed
             print("No faces detected in the frame.")

        else:
             # Encode the first detected face
             face_encodings_cam = face_recognition.face_encodings(rgb_frame)[0]

        match_1 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_1)   
        match_2 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_2)    
        match_3 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_3)    
        match_4 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_4)    




        if match_1[0]:
            name = "architha"
            current_date = datetime.now().date()  # Get the current date
            data = Model.query.filter_by(name="architha", date=current_date).with_entities(Model.task).all()
            if not data:
               msg = "You have no reminders for today"
            else:
              msg = None
            
            return render_template('info.html', data=data, name=name, msg = msg)
        
    
        elif match_2[0]:
            name = "rahul"
            data = Model.query.filter_by(name="rahul", date=current_date).with_entities(Model.task).all()
            if not data:
               msg = "You have no reminders for today"
            else:
              msg = None
            return render_template('info.html', data = data, name = name)
        
        
        elif match_3[0]:
            name = "prabhas"
            data = Model.query.filter_by(name="prabhas", date=current_date).with_entities(Model.task).all()
            if not data:
               msg = "You have no reminders for today"
            else:
              msg = None
            return render_template('info.html', data = data , name = name)
        
        
        elif match_4[0]:
            name = "bhanu"
            data = Model.query.filter_by(name="bhanu", date=current_date).with_entities(Model.task).all()
            if not data:
               msg = "You have no reminders for today"
            else:
              msg = None
            return render_template('info.html', data = data  , name = name)
        
    
        else :
            data = None
            if not data:
               msg = "You have no remainders"
            else:
              msg = None
            return render_template('info.html', data = data  , name = name)
        
             

if __name__ == '__main__':
    app.run(port = 8080 , debug = True)
