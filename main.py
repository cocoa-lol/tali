from flask import Flask, jsonify, redirect, url_for, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return "Test" #return redirect(url_for('/join'))