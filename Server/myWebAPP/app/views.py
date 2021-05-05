from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
import base64
import cv2
import numpy as np
import json
from app import app

@app.route('/')
def index():
    return "Hello World!!!"

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        img = base64.b64decode(str(request.form['image']))
        image_data = np.fromstring(img, np.uint8)
        image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        cv2.imwrite('01.png', image_data)
        resp1={
            "errorcode":0
        }
        return jsonify(resp1)
    return "success"

@app.route('/test1', methods=['GET', 'POST'])
def test1():
    return "success"

@app.errorhandler(404)
def page_not_found(e):
    return "404"