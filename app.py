from flask import Flask
from flask import render_template
from flask import request
import csv

app=Flask("myapp")

@app.route("/page", methods=["GET"])
def home():
  name=request.args.get("nm")
  roll=request.args.get("r")
  cgpa=request.args.get("cg")
  htmlcode=render_template("mymenu.html", n=name)
  return htmlcode


@app.route("/menu" )
def mymenu():
  code=render_template("myform.html" )
  return code

@app.route("/save", methods=['POST'])
def save():
  if request.method == 'POST':
    name = request.form.get('nm')
    roll = request.form.get('r')
    cgpa = request.form.get('cg')

    fieldnames = ['name', 'roll', 'cgpa']

    with open('data.csv', 'w') as inFile:
      writer = csv.DictWriter(inFile, fieldnames=fieldnames)
      writer.writerow( {'name': name, 'roll': roll, 'cgpa': cgpa} )
  return render_template("mymenu.html", n=name)
