from flask import Flask, render_template, request, redirect, url_for, session
import mastermind_lib

app = Flask(__name__)
app.secret_key = "FJ390384230HG0ESFH0EWRH308RH405438"

#@app.route("/theme")
#def index2():
#    return render_template("index2.html")

# Sample list of items
items = [
    {"id": 1, "name": "Item1"},
    {"id": 2, "name": "Item2"},
    {"id": 3, "name": "Item3"},
    {"id": 4, "name": "Item4"},
    # Add more items here
]

@app.route('/test')
def index():
    return render_template('test.html', items=items)

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
    app.run(debug=True)