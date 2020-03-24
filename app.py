from flask import Flask, request
import cv2
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Face Detection in Video & Image</h1>"


if __name__ == "__main__":
    app.run(debug=True)