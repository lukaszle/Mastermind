from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO
from flask_socketio import emit

import mastermind_lib

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "FJ390384230HG0ESFH0EWRH308RH405438"

#@app.route("/theme")
#def index2():
#    return render_template("index2.html")

# Sample list of items
items = [
    {"id": 0, "name": "Item0"},
    {"id": 1, "name": "Item1"},
    {"id": 2, "name": "Item2"},
    {"id": 3, "name": "Item3"},
    {"id": 4, "name": "Item4"},
    {"id": 5, "name": "Item5"},
    {"id": 6, "name": "Item6"},
    {"id": 7, "name": "Item7"},
    {"id": 8, "name": "Item8"},
    {"id": 9, "name": "Item9"},
    # Add more items here
]
#Plansza mastermind w formie tablicy podłączona do przycisków
@app.route('/test')
def index():
    return render_template('test.html', items=items)
#Przyciski z linkiem do wysyłania liter.
def process_form():
    # Access form data using request.form
    #selected_color = request.form.get('A')  # Replace 'A' with the actual name of the button clicked
    a = request.form.get["A"]
    b = request.form.get["B"]
    c = request.form.get["C"]
    d = request.form.get["D"]
    # Process the selected color here
    print(A)
    return True

@socketio.on('TestEvent')
def handle_message(data):
    print('received message: ' + str(data))

@app.route("/theme", methods=["GET", "POST"])
def mastermind():
    if "secret" not in session:
        session["secret"] = mastermind_lib.code()
        session["attempts"] = 0
        session["feedback"] = []

    if request.method == "POST":
        x = request.form["guess"]
        print(A)
        x = x.upper()
        guess = list(x)
        feedback = mastermind_lib.check_code(session["secret"], guess)
 
        session["feedback"].append({"guess": guess, "feedback": feedback})
        session["attempts"] += 1
        attempts = session["attempts"]
        if feedback == ["X","X","X","X"]:
            return redirect(url_for('win'))
        if attempts == 10:
            return redirect(url_for("loose"))
    return render_template("index2.html", attempts=session["attempts"], feedback=session["feedback"], items=items)

@app.route("/newgame")
def new_game():
    session["secret"] = mastermind_lib.code()
    session["attempts"] = 0
    session["feedback"] = []
    return render_template("newgame.html")

@app.route("/win")
def win():
    return render_template("win.html", secret=session["secret"])
@app.route("/loose")
def loose():
    return render_template("loose.html", secret=session["secret"])
if __name__ == "__main__":
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)