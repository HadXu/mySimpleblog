# coding:utf-8
import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = "121234123412341234123412341234"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<filename>')
def send_image(filename):
    return send_from_directory(app.static_folder + '\images', filename)


@app.route('/gallery')
def get_gallery():
    image_names = os.listdir(app.static_folder + '\images')
    return render_template('gallery.html', image_names=image_names)


if __name__ == '__main__':
    app.run(debug=True)
