from flask import Flask, render_template,request

from datetime import datetime,date


app=Flask(__name__)

@app.route('/')
def Home():
    return render_template("Homepage.html")

@app.route('/About')
def About():
    return render_template("About.html")

if __name__ =="__main__":
    app.run(debug=True)
