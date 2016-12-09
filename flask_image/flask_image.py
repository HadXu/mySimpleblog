# coding:utf-8
import os

from flask import Flask, render_template, send_from_directory, Response

from camera import Camera

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<filename>')
def send_image(filename):
    return send_from_directory(app.static_folder + '\images', filename)


@app.route('/gallery')
def get_gallery():
    image_names = os.listdir(app.static_folder + '\images')
    return render_template('gallery.html', image_names=image_names)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video')
def video():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
