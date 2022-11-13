from flask import Flask, render_template, redirect, url_for, request, send_from_directory, send_file
from pyscrs.hallCreate import arrangeRollNo
import os

app = Flask('__name__')

app.secret_key = "437437437437"

@app.route("/")
def indexPage():
    return render_template("index.html")
@app.route("/hall", methods=["POST"])
def hallArranged():
    if request.method == "POST":
        halls = request.form["HALLS"]
        rollNos = request.files["ROLLNOS"]
        rollNos.save("data/rolls.txt")
        ttlHalls, ttlRolls, lenHall = arrangeRollNo(halls)
        print(halls)
        return render_template("hall.html", hall=ttlHalls, roll=ttlRolls, lenHall=lenHall)

@app.route("/download")
def downloadFile():
    return send_file("data/hall.xlsx", as_attachment=True)

if '__main__' == __name__:
    app.run(debug=True)