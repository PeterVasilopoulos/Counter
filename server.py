from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "x0r6ztGiggle"

@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    if 'page_count' in session:
        session['page_count'] += 1
    else:
        session['page_count'] = 1
    return render_template("counter.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/increase_by_num', methods=["POST"])
def increase_by_num():
    increase = int(request.form['num']) - 1
    session['count'] += increase
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)