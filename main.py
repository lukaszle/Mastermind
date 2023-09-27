from flask import Flask, render_template, request, redirect, url_for, session
import mastermind_lib

app = Flask(__name__)
app.secret_key = 'FJ390384230HG0ESFH0EWRH308RH405438'

@app.route("/", methods=['GET', 'POST'])
def mastermind():
    if 'secret' not in session:
        session['secret'] = mastermind_lib.code()
        session['attempts'] = 0
        session['feedback'] = []

    if request.method == 'POST':
        guess = list(request.form['guess'])
        feedback = mastermind_lib.check_code(session['secret'], guess)
        session['feedback'].append({'guess': guess, 'feedback': feedback})
        session['attempts'] += 1
    return render_template('index.html', attempts=session['attempts'], feedback=session['feedback'])

if __name__ == '__main__':
    app.run(debug=True)