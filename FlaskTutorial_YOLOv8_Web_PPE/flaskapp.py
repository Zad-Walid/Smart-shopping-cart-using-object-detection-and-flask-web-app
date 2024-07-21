from flask import Flask, render_template, Response, jsonify, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, DecimalRangeField, IntegerRangeField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired, NumberRange
import os
import cv2
from YOLO_Video import video_detection
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'zad'
app.config['UPLOAD_FOLDER'] = 'static/files'
socketio = SocketIO(app)

def generate_frames(path_x=''):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref, buffer = cv2.imencode('.jpg', detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    session.clear()
    return render_template('indexproject.html')

@app.route("/webcam", methods=['GET', 'POST'])
def webcam():
    session.clear()
    return render_template('ui.html')

@app.route('/webapp')
def webapp():
    return render_template('ui.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/qr_code')
def qr_code():
    return render_template('qr_code.html')

@app.route('/redirect_home')
def redirect_home():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
