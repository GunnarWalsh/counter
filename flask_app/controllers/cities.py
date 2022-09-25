from flask_app import app 
from flask import render_template, request, redirect, session

@app.route('/')
def refresh():
    if "number" not in session:
        session["number"] = 0
    else:
        session['number'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    if "number" not in session:
        session["number"] = 0
    else:
        session['number'] += 1
    return redirect('/')