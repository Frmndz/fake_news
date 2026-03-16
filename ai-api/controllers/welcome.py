from flask import render_template

def show_welcome():
    return render_template("welcome.html")