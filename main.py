from flask import Flask, jsonify, redirect, url_for, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return "Test" #return redirect(url_for('/join'))

if __name__ == "__main__":
    port = 80
    desc = {'path': '/'}
    zeroconf.register_service(service)
    print(f"[+] Up!")
    try:
        serve(app, host="0.0.0.0", port=port)
    finally:
        exit()
